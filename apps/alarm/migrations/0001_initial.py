# Generated by Django 5.0.1 on 2024-02-01 04:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rooms', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alarm_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_alarms', to='rooms.room')),
                ('alarm_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_alarms', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
