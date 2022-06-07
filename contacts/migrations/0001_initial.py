# Generated by Django 3.2 on 2022-06-03 07:00

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.CharField(max_length=200)),
                ('listing_id', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('appointment_date', models.DateTimeField(null=True)),
                ('message', models.TextField()),
                ('contact_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.CharField(max_length=200)),
                ('listing_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('contact_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user_id', models.IntegerField(blank=True)),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'property inquiries',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('contact_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('attachment', models.FileField(blank=True, default=None, upload_to='contact_us/attachments/%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'contactus',
                'verbose_name_plural': 'contact us',
            },
        ),
        migrations.CreateModel(
            name='PropertyRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_title', models.CharField(max_length=250)),
                ('property_type', models.CharField(max_length=250)),
                ('avail_for', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('bedroom', models.IntegerField()),
                ('bathroom', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('address', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('pincode', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^0?[5-9]{1}\\d{9}$')])),
                ('secondary_phone', models.CharField(blank=True, help_text='(Optional)', max_length=11, validators=[django.core.validators.RegexValidator('^0?[5-9]{1}\\d{9}$')])),
                ('contact_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'PropertyRequest',
                'verbose_name_plural': 'Propety Post Requests',
            },
        ),
    ]