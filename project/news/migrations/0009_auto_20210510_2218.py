# Generated by Django 3.2.2 on 2021-05-10 19:18

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_alter_artiles_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artiles',
            name='fill_text',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='artiles',
            name='title',
            field=ckeditor.fields.RichTextField(default='Мая первая статья', max_length=300, verbose_name='Название'),
        ),
    ]
