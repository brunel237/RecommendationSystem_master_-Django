# Generated by Django 4.2.7 on 2023-11-23 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_api', '0010_alter_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
