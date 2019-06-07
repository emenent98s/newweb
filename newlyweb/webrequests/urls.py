from django.conf.urls import url
from . import views

app_name="webrequests"
urlpatterns = [
    #/webrequests/
    url(r'^$',views.IndexView.as_view(),name='index'),

    url(r'^register/$',views.UserFormView.as_view(),name='register'),

    #webrequest followed by some id
    #/webrequests/<File_id>/
    url(r'^(?P<pk>[0-9]+)$',views.DetailView.as_view(),name='detail'),

    #/webrequests/file/add/
    url(r'file/add/$',views.FileCreate.as_view(),name='File-Add'),

    #/webrequests/file/2/
    url(r'file/(?P<pk>[0-9]+)/$',views.FileUpdate.as_view(),name='File-Update'),

    #/webrequests/file/2/delete/
    url(r'file/(?P<pk>[0-9]+)/delete/$',views.FileDelete.as_view(),name='File-Delete'),




]