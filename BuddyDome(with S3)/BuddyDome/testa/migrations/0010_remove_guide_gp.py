# Generated by Django 4.1.4 on 2023-01-29 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testa', '0009_alter_guide_gp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guide',
            name='gp',
        ),
    ]
