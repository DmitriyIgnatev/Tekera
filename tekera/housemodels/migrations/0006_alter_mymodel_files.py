# Generated by Django 4.1.7 on 2023-03-13 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housemodels', '0005_alter_mymodel_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='files',
            field=models.FileField(upload_to='models', verbose_name='модель здания'),
        ),
    ]