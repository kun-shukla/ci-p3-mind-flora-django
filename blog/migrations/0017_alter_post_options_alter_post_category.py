# Generated by Django 4.2.11 on 2024-04-07 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_sharediscoveryformbgvid_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['category']},
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=50),
        ),
    ]