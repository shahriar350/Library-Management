# Generated by Django 3.2.4 on 2021-07-03 09:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0007_book_isbn'),
        ('student_app', '0004_alter_borrow_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 10, 15, 58, 5, 959070)),
        ),
        migrations.AlterUniqueTogether(
            name='borrow',
            unique_together={('book', 'student')},
        ),
    ]
