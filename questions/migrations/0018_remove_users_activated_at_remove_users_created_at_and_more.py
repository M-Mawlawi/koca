# Generated by Django 4.0.3 on 2022-04-12 01:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0017_users_activated_at_users_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='activated_at',
        ),
        migrations.RemoveField(
            model_name='users',
            name='created_at',
        ),
        migrations.AddField(
            model_name='users',
            name='expire',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
