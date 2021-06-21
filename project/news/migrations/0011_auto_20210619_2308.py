# Generated by Django 3.2.2 on 2021-06-19 20:08

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_artiles_essence'),
    ]

    operations = [
        migrations.AddField(
            model_name='artiles',
            name='anons',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Анонс'),
        ),
        migrations.AlterField(
            model_name='artiles',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата публикации'),
        ),
    ]
