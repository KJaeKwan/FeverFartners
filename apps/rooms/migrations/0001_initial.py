# Generated by Django 5.0.1 on 2024-02-01 04:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=100)),
                ('rule', models.CharField(max_length=100)),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms_managed', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='rooms_joined', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AuthenticationImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='authentication_images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('is_authenticated', models.BooleanField(default=False, verbose_name='인증여부')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authentication_images', to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authentication_images', to='rooms.room')),
            ],
        ),
    ]
