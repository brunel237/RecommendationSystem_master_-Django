# Generated by Django 4.2.5 on 2023-10-19 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_api', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academiclevel',
            name='level',
            field=models.CharField(choices=[('l1', 'Level 1'), ('l2', 'Level 2'), ('l3', 'Level 3'), ('m1', 'Master 1'), ('m2', 'Master 2'), ('predoc', 'Pre Doctorate')], max_length=10),
        ),
    ]
