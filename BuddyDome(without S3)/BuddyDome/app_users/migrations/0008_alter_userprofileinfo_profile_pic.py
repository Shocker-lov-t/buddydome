# Generated by Django 4.1.4 on 2023-01-12 21:39

import app_users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0007_alter_userprofileinfo_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(upload_to=app_users.models.path_and_rename, verbose_name='Profile Picture'),
        ),
    ]
