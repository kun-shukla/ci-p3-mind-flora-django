# Generated by Django 4.2.11 on 2024-04-07 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_on', 'category']},
        ),
    ]