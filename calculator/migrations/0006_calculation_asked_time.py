# Generated by Django 3.0.7 on 2020-06-26 20:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0005_auto_20200626_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculation',
            name='asked_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]