# Generated by Django 4.2.5 on 2023-10-19 16:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_api', '0002_initial'),
        ('users_api', '0002_alter_lecturer_lectures_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='biography',
            field=models.TextField(default='None'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='field_of_research',
            field=models.CharField(default='None', max_length=255),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='followers',
            field=models.ManyToManyField(blank=True, null=True, related_name='lecturer_followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='lectures',
            field=models.ManyToManyField(blank=True, null=True, related_name='lectures', to='courses_api.academiclevelcourse'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='title',
            field=models.CharField(choices=[('phd', 'PhD'), ('pr', 'Professor')], max_length=5),
        ),
        migrations.AlterField(
            model_name='schoolelder',
            name='courses_attending',
            field=models.ManyToManyField(blank=True, null=True, related_name='school_elders_courses', to='courses_api.academiclevelcourse'),
        ),
        migrations.AlterField(
            model_name='schoolelder',
            name='followers',
            field=models.ManyToManyField(blank=True, null=True, related_name='school_elder_followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student',
            name='courses_attending',
            field=models.ManyToManyField(blank=True, null=True, related_name='student_courses', to='courses_api.academiclevelcourse'),
        ),
    ]
