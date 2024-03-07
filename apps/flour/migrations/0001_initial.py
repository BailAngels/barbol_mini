# Generated by Django 5.0.2 on 2024-02-29 10:58

import ckeditor.fields
import utils.image_path
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название')),
                ('description', ckeditor.fields.RichTextField(verbose_name='описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена')),
                ('image', models.ImageField(upload_to=utils.image_path.upload_flour, verbose_name='изображение')),
            ],
            options={
                'verbose_name': 'Мучное',
                'verbose_name_plural': 'Мучные',
            },
        ),
    ]
