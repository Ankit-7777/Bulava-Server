# Generated by Django 5.0.4 on 2024-05-10 12:14

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('category_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('message', models.TextField(max_length=300, verbose_name='Message')),
            ],
        ),
        migrations.CreateModel(
            name='CoverImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='covers/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_category_type', to='WeddingApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('guest_of_honor', models.CharField(blank=True, max_length=100, null=True, verbose_name='Guest of Honor')),
                ('organizer_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Organizer Name')),
                ('phone_number', models.CharField(help_text="Please provide organizer's contact number.", max_length=10, verbose_name='Phone Number')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Description')),
                ('event_date', models.DateField(verbose_name='Event Date')),
                ('event_start_time', models.TimeField(verbose_name='Event Start Time')),
                ('event_end_time', models.TimeField(verbose_name='Event End Time')),
                ('venue_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Venue Name')),
                ('venue_address', models.CharField(max_length=200, verbose_name='Venue Address')),
                ('venue_pin_code', models.CharField(max_length=6, verbose_name='Venue Pin Code')),
                ('is_published', models.BooleanField(default=False, verbose_name='Is Published')),
                ('max_guests', models.PositiveIntegerField(blank=True, default=100, null=True, verbose_name='Maximum Guests')),
                ('gift_sending_link', models.URLField(blank=True, null=True, verbose_name='Gift Sending Link')),
                ('theme', models.CharField(blank=True, max_length=100, null=True, verbose_name='Theme')),
                ('dress_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Dress Code')),
                ('bride_name', models.CharField(blank=True, max_length=100, null=True, verbose_name="Bride's Name")),
                ('groom_name', models.CharField(blank=True, max_length=100, null=True, verbose_name="Groom's Name")),
                ('bride_mother_name', models.CharField(blank=True, max_length=100, null=True, verbose_name="Bride's Mother Name")),
                ('bride_father_name', models.CharField(blank=True, max_length=100, null=True, verbose_name="Bride's Father Name")),
                ('groom_mother_name', models.CharField(blank=True, max_length=100, null=True, verbose_name="Groom's Mother Name")),
                ('groom_father_name', models.CharField(blank=True, max_length=100, null=True, verbose_name="Groom's Father Name")),
                ('bride_age', models.PositiveIntegerField(blank=True, null=True, verbose_name="Bride's Age")),
                ('groom_age', models.PositiveIntegerField(blank=True, null=True, verbose_name="Groom's Age")),
                ('birthday_person_name', models.CharField(blank=True, max_length=100, null=True, verbose_name="Birthday Person's Name")),
                ('birthday_person_age', models.PositiveIntegerField(blank=True, null=True, verbose_name="Birthday Person's Age")),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('event_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_category', to='WeddingApp.category')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(blank=True, null=True)),
                ('is_attending', models.BooleanField(default=False)),
                ('dietary_restrictions', models.TextField(blank=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guests', to='WeddingApp.event')),
            ],
        ),
        migrations.CreateModel(
            name='RSVP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Maybe', 'Maybe')], max_length=10)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rsvps', to='WeddingApp.event')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rsvps', to='WeddingApp.guest')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('service', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=20, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendors', to='WeddingApp.event')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('full_name', models.CharField(max_length=255, verbose_name='Full Name')),
                ('phone', models.CharField(max_length=10, verbose_name='Phone')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.CharField(default='User', max_length=10, verbose_name='Role')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
