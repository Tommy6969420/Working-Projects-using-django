# Generated by Django 4.2.4 on 2023-08-16 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0003_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='otp',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='otp',
            name='password',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]