# Generated by Django 3.0.7 on 2020-06-27 19:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_auto_20200627_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydata',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 27, 19, 25, 47, 27842, tzinfo=utc)),
        ),
    ]
