# Generated by Django 2.1.5 on 2019-09-01 13:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsapp', '0014_auto_20190901_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='case_id',
        ),
        migrations.RemoveField(
            model_name='visits',
            name='case_id',
        ),
        migrations.AlterField(
            model_name='case',
            name='last_visit',
            field=models.DateField(default=datetime.datetime(2019, 9, 1, 18, 53, 0, 505642)),
        ),
        migrations.AlterField(
            model_name='case',
            name='starting_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 1, 18, 53, 0, 505642)),
        ),
    ]
