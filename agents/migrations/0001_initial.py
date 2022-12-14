# Generated by Django 3.2 on 2022-06-13 07:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_ID', models.CharField(max_length=8)),
                ('designation', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(max_length=13)),
                ('photo', imagekit.models.fields.ProcessedImageField(upload_to='images/supervisors/%Y/%m/%d/')),
                ('is_mvp', models.BooleanField(default=False)),
                ('hire_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('Department', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='agents.department')),
                ('email', models.OneToOneField(limit_choices_to={'is_active': True, 'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_ID', models.CharField(max_length=8)),
                ('photo', imagekit.models.fields.ProcessedImageField(upload_to='images/agents/%Y/%m/%d/')),
                ('designation', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=13)),
                ('is_mvp', models.BooleanField(default=False)),
                ('hire_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('Department', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='agents.department')),
                ('email', models.OneToOneField(limit_choices_to={'is_active': True, 'is_realtor': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('supervisor_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='agents.supervisor')),
            ],
        ),
    ]
