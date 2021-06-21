# Generated by Django 3.2.2 on 2021-05-08 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home_text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Мая первая статья', max_length=50, verbose_name='Название')),
                ('fill_text', models.TextField(verbose_name='Статья')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Информация на главной странице',
                'verbose_name_plural': 'Информации на главной странице',
            },
        ),
    ]