# Generated by Django 4.2.5 on 2023-10-08 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
