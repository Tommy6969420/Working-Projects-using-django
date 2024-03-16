# Generated by Django 4.2.6 on 2023-10-18 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('std_class', models.CharField(max_length=10)),
                ('section', models.CharField(max_length=10)),
                ('roll_no', models.CharField(max_length=3)),
                ('address', models.CharField(max_length=64)),
                ('parents_name', models.CharField(max_length=64)),
                ('contact', models.CharField(max_length=10)),
                ('std_photo', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]
