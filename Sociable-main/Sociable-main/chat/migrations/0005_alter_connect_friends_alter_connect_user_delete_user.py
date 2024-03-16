# Generated by Django 4.2.4 on 2024-03-13 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_contact_number'),
        ('chat', '0004_messaging_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connect',
            name='friends',
            field=models.ManyToManyField(related_name='reciever', to='users.user'),
        ),
        migrations.AlterField(
            model_name='connect',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user', unique=True),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
