# Generated by Django 3.2.2 on 2021-05-11 16:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210511_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text_home',
            name='title',
            field=ckeditor.fields.RichTextField(max_length=300, verbose_name='Название'),
        ),
    ]