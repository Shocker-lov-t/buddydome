# Generated by Django 4.1.4 on 2023-01-12 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0002_alter_userprofileinfo_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user_type',
            field=models.CharField(choices=[('contributor', 'contributor'), ('student', 'student'), ('employee', 'employee')], default='student', max_length=15),
        ),
    ]
