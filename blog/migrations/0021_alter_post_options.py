# Generated by Django 4.2.11 on 2024-04-07 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['category', 'created_on']},
        ),
    ]
