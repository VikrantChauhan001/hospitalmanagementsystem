# Generated by Django 2.1.5 on 2019-09-06 06:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hmsapp', '0035_auto_20190906_0409'),
    ]

    operations = [
        migrations.AddField(
            model_name='visits',
            name='time',
            field=models.TimeField(default='00:00'),
        ),
        migrations.AlterField(
            model_name='case',
            name='starting_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 6, 6, 28, 25, 69561, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='visits',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 9, 6, 6, 28, 25, 69561, tzinfo=utc)),
        ),
    ]
