from django.db import models
from tinymce import models as tinymce_models
from sorl.thumbnail import get_thumbnail, delete
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete


class MyModel(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False)
    descriptions = tinymce_models.HTMLField(
        verbose_name='Описание',
        blank=False,
        null=False)
    gltf = models.FileField(
        upload_to='models',
        verbose_name='gltf-файл',
        blank=False,
        null=False)
    binn = models.ManyToManyField(
        'Bin',
        blank=False,
        null=False)
    textures = models.ManyToManyField(
        'Textures',
        blank=False,
        null=False)
    img = models.ImageField(
        'Фото карточки, размер 250*200 px'
    )

    @property
    def get_md(self):
        return get_thumbnail(
            self.files,
            '300x300',
            crop='center',
            quality=51)

    def md_tmb(self):
        if self.files:
            return mark_safe(
                f"{self.get_md.url}"
            )
        return 'нет модели'

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)


class Textures(models.Model):
    textures = models.FileField(
        upload_to='models/textures',
        verbose_name='Текстуры для модели',
        blank=False,
        null=False)


class Bin(models.Model):
    binn = models.FileField(
        upload_to='models',
        verbose_name='bin-файлы',
        blank=False,
        null=False)


class Application(models.Model):
    name = models.CharField(
        'Имя',
        max_length=255,
        blank=False,
        null=False
    )

    phone = models.CharField(
        'Номер телефона для связи',
        max_length=255,
        blank=False,
        null=False
    )

    house = models.ForeignKey(MyModel, on_delete=models.CASCADE)
