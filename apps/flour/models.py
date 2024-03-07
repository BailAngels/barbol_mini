import os
from django.db import models
from utils.image_path import upload_flour
from ckeditor.fields import RichTextField


class Flour(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="название"
    )
    description = RichTextField(
        verbose_name="описание"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="цена"
    )
    image = models.ImageField(
        upload_to=upload_flour,
        verbose_name="изображение"
    )

    def delete(self, using=None, keep_parents=False):
        os.remove(self.image.path)
        super().delete(using=None, keep_parents=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мучное"
        verbose_name_plural = "Мучные"


