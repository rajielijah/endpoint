# Generated by Django 3.0.7 on 2020-09-09 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endApi', '0019_auto_20200909_1604'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='company_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(default='ondo', max_length=200),
            preserve_default=False,
        ),
    ]