# Generated by Django 3.0.8 on 2020-08-06 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_note_important'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='important',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
