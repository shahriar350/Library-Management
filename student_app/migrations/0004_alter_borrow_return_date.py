# Generated by Django 3.2.4 on 2021-07-03 09:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0003_alter_borrow_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 10, 15, 34, 57, 858216)),
        ),
    ]