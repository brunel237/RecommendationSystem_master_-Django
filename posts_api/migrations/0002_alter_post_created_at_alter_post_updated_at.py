# Generated by Django 4.2.5 on 2023-10-03 12:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 3, 12, 7, 46, 866464, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 3, 12, 7, 46, 866479, tzinfo=datetime.timezone.utc)),
        ),
    ]