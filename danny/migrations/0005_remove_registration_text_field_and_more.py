# Generated by Django 4.1.2 on 2022-11-03 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('danny', '0004_registration_text_field_registration_url_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='text_field',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='url_field',
        ),
    ]
