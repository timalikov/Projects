# Generated by Django 4.2 on 2023-05-04 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_username_user_firstname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='firstName',
            new_name='username',
        ),
    ]