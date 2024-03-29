# Generated by Django 4.2.7 on 2023-11-15 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts_api', '0010_remove_post_media_postmedia'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='media')),
                ('file_type', models.CharField(blank=True, max_length=255, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media_post', to='posts_api.post')),
            ],
        ),
    ]
