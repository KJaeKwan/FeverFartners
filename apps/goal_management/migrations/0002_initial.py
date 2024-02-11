# Generated by Django 5.0.1 on 2024-02-11 02:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("goal_management", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="goal",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="goal",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="tag",
            name="parent_tag",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="goal_management.tag",
            ),
        ),
        migrations.AddField(
            model_name="goal",
            name="tags",
            field=models.ManyToManyField(default=None, to="goal_management.tag"),
        ),
    ]
