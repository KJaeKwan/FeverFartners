# Generated by Django 5.0.1 on 2024-02-06 10:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nickname', models.CharField(max_length=30, unique=True)),
                ('profile', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/%Y/%m/%d/')),
                ('region', models.CharField(blank=True, max_length=30, null=True)),
                ('region_detail', models.CharField(blank=True, max_length=30, null=True)),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('fuel', models.IntegerField(blank=True, default=100, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]
