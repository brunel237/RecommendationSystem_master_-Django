# Generated by Django 4.2.5 on 2023-10-03 00:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messages_api', '0005_alter_chat_created_at_alter_message_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 10, 3, 0, 8, 47, 933199, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 10, 3, 0, 8, 47, 933681, tzinfo=datetime.timezone.utc)),
        ),
    ]
