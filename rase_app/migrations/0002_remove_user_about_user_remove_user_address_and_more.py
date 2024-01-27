# Generated by Django 4.2.4 on 2024-01-09 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rase_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='about_user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email_active_code',
        ),
        migrations.AddField(
            model_name='user',
            name='admin',
            field=models.BooleanField(default=False, verbose_name='is_admin'),
        ),
    ]
