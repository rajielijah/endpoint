# Generated by Django 3.0.7 on 2020-09-08 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endApi', '0015_auto_20200908_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default='me', max_length=100),
            preserve_default=False,
        ),
    ]