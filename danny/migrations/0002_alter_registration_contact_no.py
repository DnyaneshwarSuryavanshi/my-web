# Generated by Django 4.1.2 on 2022-11-02 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danny', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='contact_no',
            field=models.IntegerField(max_length=10),
        ),
    ]
