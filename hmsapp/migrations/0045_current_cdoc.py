# Generated by Django 2.1.5 on 2019-09-10 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsapp', '0044_auto_20190908_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='current',
            name='cdoc',
            field=models.IntegerField(default=1),
        ),
    ]