# Generated by Django 2.1.5 on 2019-09-05 11:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsapp', '0030_auto_20190905_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='last_visit',
            field=models.DateField(default=datetime.datetime(2019, 9, 5, 17, 23, 44, 729660)),
        ),
        migrations.AlterField(
            model_name='case',
            name='starting_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 5, 17, 23, 44, 729660)),
        ),
    ]