# Generated by Django 3.0.6 on 2020-05-16 18:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('phonenumber', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex='^[0-9]{10}$')])),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
