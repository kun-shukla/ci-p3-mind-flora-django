# Generated by Django 4.2.11 on 2024-04-06 13:46

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutsectionnavimage',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]