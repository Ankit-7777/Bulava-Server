# Generated by Django 5.0.6 on 2024-07-18 09:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeddingApp', '0024_group_uuid_userevent_uuid_alter_group_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='group_owner', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Birth'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='occasion',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Occasion'),
        ),
        migrations.RemoveField(
            model_name='group',
            name='member',
        ),
        migrations.AddField(
            model_name='group',
            name='member',
            field=models.ManyToManyField(related_name='group_members', to=settings.AUTH_USER_MODEL),
        ),
    ]
