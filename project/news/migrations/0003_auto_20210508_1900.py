# Generated by Django 3.2.2 on 2021-05-08 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210508_1001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Downloader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('Dis', models.TextField(max_length=1000, verbose_name='Описание')),
                ('file', models.FileField(upload_to='media/', verbose_name='Видео')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]