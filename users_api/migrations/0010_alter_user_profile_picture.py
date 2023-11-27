# Generated by Django 4.2.7 on 2023-11-21 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_api', '0009_alter_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.FileField(blank=True, default='profile_default.png', null=True, upload_to='profile_pictures'),
        ),
    ]
