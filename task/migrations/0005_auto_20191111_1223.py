# Generated by Django 2.2.7 on 2019-11-11 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_outputmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='input_minutes',
            field=models.IntegerField(default=0, verbose_name='минут'),
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='input_seconds',
            field=models.IntegerField(default=0, verbose_name='секунд'),
        ),
    ]
