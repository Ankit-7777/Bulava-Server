# Generated by Django 5.0.4 on 2024-05-09 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeddingApp', '0002_alter_event_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Id'),
        ),
    ]
