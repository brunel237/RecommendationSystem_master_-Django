# Generated by Django 4.2.5 on 2023-10-01 23:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_api', '0009_alter_chat_created_at_alter_forum_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 10, 1, 23, 53, 47, 58667, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='forum',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 10, 1, 23, 53, 47, 59890, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 10, 1, 23, 53, 47, 59194, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='participantsforum',
            name='entry_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 10, 1, 23, 53, 47, 60441, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 1, 23, 53, 47, 53710, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 1, 23, 53, 47, 53738, tzinfo=datetime.timezone.utc)),
        ),
    ]