# Generated by Django 4.2.5 on 2023-10-02 22:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messages_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 10, 2, 22, 59, 2, 687255, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 10, 2, 22, 59, 2, 687772, tzinfo=datetime.timezone.utc)),
        ),
    ]
