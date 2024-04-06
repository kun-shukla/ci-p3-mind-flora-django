# Generated by Django 4.2.11 on 2024-04-06 21:09

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_sharediscoveryformbgvid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharediscoveryformbgvid',
            name='featured_video',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='video'),
        ),
    ]
