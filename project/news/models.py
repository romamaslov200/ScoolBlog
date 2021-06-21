from django import forms
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Artiles(models.Model):
    title = RichTextField('Название', max_length=300, default='Мая первая статья')
    anons = RichTextField('Анонс', blank=True)
    fill_text = RichTextField('Статья', blank=True)
    date = models.DateTimeField('Дата публикации', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новасти'


class Downloader(models.Model):
    name = models.CharField("Название", max_length=100)
    Dis = models.TextField("Описание", max_length=1000)
    file = models.FileField("Видео", upload_to='media/')

