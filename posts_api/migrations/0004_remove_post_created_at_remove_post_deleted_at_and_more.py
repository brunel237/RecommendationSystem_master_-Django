# Generated by Django 4.2.5 on 2023-10-18 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts_api', '0003_post_is_deleted_alter_post_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_at',
        ),
    ]