# Generated by Django 3.2.4 on 2021-07-03 08:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrow',
            name='is_returned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='borrow',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 10, 14, 21, 38, 366774)),
        ),
    ]
