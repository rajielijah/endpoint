# Generated by Django 3.0.7 on 2020-09-03 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endApi', '0003_profile_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='images',
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=100),
        ),
    ]
