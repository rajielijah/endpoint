# Generated by Django 3.0.7 on 2020-09-08 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('endApi', '0014_auto_20200908_1923'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='user',
        ),
    ]
