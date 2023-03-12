# Generated by Django 4.1.7 on 2023-03-12 07:22

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('descriptions', tinymce.models.HTMLField(verbose_name='Описание')),
                ('files', models.FileField(upload_to='textur/')),
            ],
        ),
    ]
