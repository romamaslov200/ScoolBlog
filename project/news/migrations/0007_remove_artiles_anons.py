# Generated by Django 3.2.2 on 2021-05-10 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_artiles_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artiles',
            name='anons',
        ),
    ]
