from django.db import models
from tinymce import models as tinymce_models


class MyModel(models.Model):
    name = models.CharField(max_length=255)
    descriptions = tinymce_models.HTMLField(verbose_name='Описание')
    files = models.ManyToManyField('FileModel', blank=True)


class FileModel(models.Model):
    file = models.FileField(upload_to='textur/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
