# Generated by Django 2.1.5 on 2019-09-01 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsapp', '0010_auto_20190901_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='last_visit',
            field=models.DateField(default=datetime.datetime(2019, 9, 1, 18, 41, 28, 124205)),
        ),
        migrations.AlterField(
            model_name='case',
            name='starting_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 1, 18, 41, 28, 124205)),
        ),
    ]