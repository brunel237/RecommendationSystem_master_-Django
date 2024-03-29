# Generated by Django 4.2.5 on 2023-09-30 14:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, null=True)),
                ('media', models.FileField(blank=True, null=True, upload_to='')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 9, 30, 14, 33, 54, 9477, tzinfo=datetime.timezone.utc))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2023, 9, 30, 14, 33, 54, 9492, tzinfo=datetime.timezone.utc))),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
