# Generated by Django 4.2.4 on 2023-08-14 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
    ]