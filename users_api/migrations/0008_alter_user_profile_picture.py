# Generated by Django 4.2.7 on 2023-11-19 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_api', '0007_alter_user_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.TextField(blank=True, null=True),
        ),
    ]