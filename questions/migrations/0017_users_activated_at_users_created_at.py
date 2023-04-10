# Generated by Django 4.0.3 on 2022-04-12 01:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0016_alter_users_tel'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='activated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
