# Generated by Django 3.0.5 on 2020-06-06 09:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='start_time',
            field=models.DateTimeField(verbose_name=django.utils.timezone.now),
        ),
    ]
