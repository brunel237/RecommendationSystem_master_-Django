# Generated by Django 4.2.5 on 2023-11-05 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_api', '0004_alter_lecturer_followers_alter_lecturer_lectures_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_default.png', null=True, upload_to='profile_pictures'),
        ),
    ]
