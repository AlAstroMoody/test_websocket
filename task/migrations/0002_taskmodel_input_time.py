# Generated by Django 2.2.7 on 2019-11-10 09:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='input_time',
            field=models.DurationField(default='00:00', verbose_name=datetime.timedelta(seconds=605)),
        ),
    ]
