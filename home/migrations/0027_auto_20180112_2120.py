# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-12 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_auto_20180111_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordinatorapproval',
            name='approval_status',
            field=models.CharField(choices=[('P', 'Pending'), ('W', 'Withdrawn'), ('R', 'Rejected'), ('A', 'Approved')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='coordinatorapproval',
            name='reason_denied',
            field=models.CharField(blank=True, help_text='\n            Please explain why you are withdrawing this request. This\n            explanation will only be shown to Outreachy organizers and\n            approved people within this community.\n            ', max_length=3000),
        ),
        migrations.AddField(
            model_name='mentorapproval',
            name='approval_status',
            field=models.CharField(choices=[('P', 'Pending'), ('W', 'Withdrawn'), ('R', 'Rejected'), ('A', 'Approved')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='mentorapproval',
            name='reason_denied',
            field=models.CharField(blank=True, help_text='\n            Please explain why you are withdrawing this request. This\n            explanation will only be shown to Outreachy organizers and\n            approved people within this community.\n            ', max_length=3000),
        ),
        migrations.AddField(
            model_name='participation',
            name='approval_status',
            field=models.CharField(choices=[('P', 'Pending'), ('W', 'Withdrawn'), ('R', 'Rejected'), ('A', 'Approved')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='participation',
            name='reason_denied',
            field=models.CharField(blank=True, help_text='\n            Please explain why you are withdrawing this request. This\n            explanation will only be shown to Outreachy organizers and\n            approved people within this community.\n            ', max_length=3000),
        ),
        migrations.AddField(
            model_name='project',
            name='approval_status',
            field=models.CharField(choices=[('P', 'Pending'), ('W', 'Withdrawn'), ('R', 'Rejected'), ('A', 'Approved')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='project',
            name='reason_denied',
            field=models.CharField(blank=True, help_text='\n            Please explain why you are withdrawing this request. This\n            explanation will only be shown to Outreachy organizers and\n            approved people within this community.\n            ', max_length=3000),
        ),
    ]
