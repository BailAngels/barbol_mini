import os

from django.db import models
from utils.image_path import upload_cakes
from ckeditor.fields import RichTextField


class Cake(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Название"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="цена"
    )
    description = RichTextField(
        verbose_name="описание"
    )
    image = models.ImageField(
        upload_to=upload_cakes,
        verbose_name="изображение"
    )

    def delete(self, using=None, keep_parents=False):
        os.remove(self.image.path)
        super().delete(using=None, keep_parents=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Торт"
        verbose_name_plural = "Торты"




