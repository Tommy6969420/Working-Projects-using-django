# Generated by Django 4.2.4 on 2024-02-09 10:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0018_alter_chatroom_members_alter_videocall_date_ended_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videocall',
            name='date_ended',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 9, 16, 17, 31, 177154)),
        ),
        migrations.AlterField(
            model_name='videocall',
            name='date_started',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 9, 16, 17, 31, 177154)),
        ),
    ]