# Generated by Django 4.0.3 on 2022-04-12 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0018_remove_users_activated_at_remove_users_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='is_active',
        ),
    ]
