# Generated by Django 4.1.1 on 2022-09-19 13:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_posts_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 13, 49, 51, 344468)),
        ),
    ]