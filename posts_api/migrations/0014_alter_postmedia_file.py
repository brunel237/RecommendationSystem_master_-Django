# Generated by Django 4.2.7 on 2023-11-24 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_api', '0013_alter_postmedia_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmedia',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='posts/'),
        ),
    ]
