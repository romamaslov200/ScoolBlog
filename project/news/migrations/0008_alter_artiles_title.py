# Generated by Django 3.2.2 on 2021-05-10 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_remove_artiles_anons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artiles',
            name='title',
            field=models.CharField(default='Мая первая статья', max_length=50, verbose_name='Название'),
        ),
    ]