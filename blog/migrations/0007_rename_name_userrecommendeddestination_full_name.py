# Generated by Django 4.2.11 on 2024-04-05 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_dest_title_userrecommendeddestination_destination'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userrecommendeddestination',
            old_name='name',
            new_name='full_Name',
        ),
    ]
