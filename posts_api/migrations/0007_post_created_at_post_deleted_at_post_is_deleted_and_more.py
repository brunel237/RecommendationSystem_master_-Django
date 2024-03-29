# Generated by Django 4.2.5 on 2023-11-05 17:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_api', '0006_merge_20231103_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 11, 5, 17, 48, 44, 296490, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='deleted_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 11, 5, 17, 49, 14, 788093, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 11, 5, 17, 49, 30, 680699, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
