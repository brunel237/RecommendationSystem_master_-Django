# Generated by Django 4.2.7 on 2023-11-24 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_api', '0011_alter_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.FileField(blank=True, default='profile/profile_pics/profile_default.png', null=True, upload_to='profile/profile_pics/'),
        ),
    ]