# Generated by Django 3.2.2 on 2021-05-10 14:08

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20210508_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='artiles',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, verbose_name='Видео'),
        ),
    ]
