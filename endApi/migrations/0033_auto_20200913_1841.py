# Generated by Django 3.0.7 on 2020-09-13 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endApi', '0032_auto_20200913_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endApi.Profile'),
        ),
    ]
