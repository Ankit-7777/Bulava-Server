# Generated by Django 5.0.4 on 2024-06-01 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeddingApp', '0008_userprofile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_seen',
            field=models.BooleanField(default=False, null=True),
        ),
    ]