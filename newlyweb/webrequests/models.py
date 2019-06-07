from django.db import models
from django.urls import reverse

class Files(models.Model):
    filename=models.CharField(max_length=250)
    file_type=models.CharField(max_length=10)
    upload_file=models.FileField()

    def get_absolute_url(self):
        return reverse('webrequests:detail', kwargs={'pk' :self.pk})

    def __str__(self):
        return self.filename + '-' + self.file_type