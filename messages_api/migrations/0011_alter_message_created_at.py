# Generated by Django 4.2.5 on 2023-10-03 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messages_api', '0010_alter_chat_created_at_alter_message_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
