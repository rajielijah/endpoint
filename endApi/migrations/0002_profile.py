# Generated by Django 3.0.7 on 2020-09-02 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='')),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=300)),
                ('phone', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endApi.Image')),
            ],
        ),
    ]