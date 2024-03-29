# Generated by Django 4.2.5 on 2023-10-02 22:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('messages_api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('purpose', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(verbose_name=datetime.datetime(2023, 10, 2, 22, 52, 53, 993860, tzinfo=datetime.timezone.utc))),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messages_api.chat')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('participants', models.ManyToManyField(related_name='participants_forum', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
