# Generated by Django 3.0.7 on 2020-09-08 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endApi', '0010_auto_20200908_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=10),
            preserve_default=False,
        ),
    ]
