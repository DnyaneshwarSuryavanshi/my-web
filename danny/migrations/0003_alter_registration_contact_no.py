# Generated by Django 4.1.2 on 2022-11-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danny', '0002_alter_registration_contact_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='contact_no',
            field=models.IntegerField(),
        ),
    ]
