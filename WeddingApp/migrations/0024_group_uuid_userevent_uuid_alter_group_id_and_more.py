# Generated by Django 5.0.6 on 2024-07-05 06:22

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeddingApp', '0023_event_event_id_group_userevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='userevent',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userevent',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]