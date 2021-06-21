from django.db import models
from ckeditor.fields import RichTextField

class text_home(models.Model):
    models.CharField('Суть', max_length=50, blank=True)
    title = RichTextField('Название', max_length=300)
    fill_text = RichTextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информация на главной странице'
        verbose_name_plural = 'Информации на главной странице'