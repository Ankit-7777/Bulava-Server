# Generated by Django 5.0.6 on 2024-06-05 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeddingApp', '0009_event_is_seen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='is_seen',
            field=models.BooleanField(default=False),
        ),
    ]
