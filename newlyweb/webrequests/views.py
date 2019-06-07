from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from .models import Files
from django.views.generic import View
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'webrequests/index.html'
    context_object_name ='all_files'

    def get_queryset(self):
        return Files.objects.all()

class DetailView(generic.DetailView):
    model = Files
    template_name = 'webrequests/detail.html'

class FileCreate(CreateView):
    model = Files
    fields = ['filename','file_type','upload_file']

class FileUpdate(UpdateView):
    model = Files
    fields = ['filename','file_type','upload_file']

class FileDelete(DeleteView):
    model = Files
    success_url = reverse_lazy('webrequests:index')

class UserFormView(View):
    form_class= UserForm
    template_name='webrequests/registration_form.html'

    #display BLANK form
    def get(self, request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    #process data
    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #cleaned normalized data
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns user object if Credentials are correct
            user=authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('webrequests:index')

        return render(request,self.template_name,{'form':form})



