# Generated by Django 3.2.20 on 2023-07-12 05:32

from django.db import migrations
import django_migration_linter as linter


class Migration(migrations.Migration):

    dependencies = [
        ('twilioapp', '0006_auto_20230601_0807'),
    ]

    operations = [
        linter.IgnoreMigration(),
        migrations.DeleteModel(
            name='TwilioLogRecord',
        ),
    ]