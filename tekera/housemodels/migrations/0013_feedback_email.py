# Generated by Django 4.1.7 on 2023-03-27 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housemodels', '0012_alter_feedback_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='email',
            field=models.EmailField(default=False, max_length=254, verbose_name='Ваша почта'),
            preserve_default=False,
        ),
    ]
