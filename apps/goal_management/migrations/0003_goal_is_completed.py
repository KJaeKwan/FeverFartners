# Generated by Django 5.0.1 on 2024-02-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goal_management', '0002_goal_is_in_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
