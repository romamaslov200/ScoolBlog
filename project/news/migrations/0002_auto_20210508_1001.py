# Generated by Django 3.2.2 on 2021-05-08 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('cover', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AlterModelOptions(
            name='artiles',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новасти'},
        ),
    ]