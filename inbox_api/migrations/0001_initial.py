# Generated by Django 4.2.5 on 2023-10-20 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messages_api', '0003_remove_message_chat_remove_message_sender_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inbox_guest', to=settings.AUTH_USER_MODEL)),
                ('messages', models.ManyToManyField(related_name='inbox_messages', to='messages_api.message')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inbox_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]