# Generated by Django 4.1.1 on 2022-09-19 19:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_posts_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 19, 30, 22, 319136, tzinfo=datetime.timezone.utc)),
        ),
    ]