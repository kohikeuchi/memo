# Generated by Django 3.0.8 on 2020-07-31 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_note_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='users',
        ),
    ]
