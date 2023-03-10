# Generated by Django 4.1.4 on 2023-01-19 20:16

import app_users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0010_alter_userprofileinfo_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, default='user_avatar.png', upload_to=app_users.models.path_and_rename, verbose_name='Profile Picture'),
        ),
    ]
