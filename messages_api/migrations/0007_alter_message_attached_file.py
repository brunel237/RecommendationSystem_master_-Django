# Generated by Django 4.2.7 on 2024-01-17 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messages_api', '0006_alter_message_receiver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='attached_file',
            field=models.FileField(blank=True, null=True, upload_to='chats/'),
        ),
    ]