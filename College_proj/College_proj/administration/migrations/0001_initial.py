# Generated by Django 4.2.6 on 2024-02-08 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=64)),
                ('fathers_name', models.CharField(max_length=64)),
                ('mothers_name', models.CharField(max_length=64)),
                ('date_of_birth', models.DateField(default=False)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10)),
                ('present_address', models.CharField(max_length=64)),
                ('permanent_address', models.CharField(max_length=64)),
                ('student_phone_no', models.CharField(max_length=15)),
                ('emergency_phone_no', models.CharField(max_length=15)),
                ('students_email', models.EmailField(max_length=254)),
                ('accept_terms', models.BooleanField()),
                ('admission_date', models.DateField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.class')),
            ],
        ),
    ]
