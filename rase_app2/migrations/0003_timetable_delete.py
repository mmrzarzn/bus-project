# Generated by Django 4.2.4 on 2024-01-09 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rase_app2', '0002_timetable_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='delete',
            field=models.BooleanField(default=False, verbose_name='حذف'),
        ),
    ]
