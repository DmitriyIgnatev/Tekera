from django.db import models
from tinymce import models as tinymce_models


class MyModel(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False)
    descriptions = tinymce_models.HTMLField(
        verbose_name='Описание',
        blank=False,
        null=False)
    files = models.FileField(
        upload_to='models',
        verbose_name='модель здания',
        blank=False,
        null=False)
    textures = models.ManyToManyField(
        'Textures',
        blank=False,
        null=False)


class Textures(models.Model):
    textures = models.FileField(
        upload_to='models/textures',
        verbose_name='Текстуры для модели',
        blank=False,
        null=False)
