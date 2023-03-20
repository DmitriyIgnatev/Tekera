# Generated by Django 4.1.7 on 2023-03-20 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('housemodels', '0008_mymodel_img_alter_bin_binn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housemodels.mymodel')),
            ],
        ),
    ]