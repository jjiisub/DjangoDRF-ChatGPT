# Generated by Django 4.2.3 on 2023-07-28 13:24

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0006_alter_chatingroom_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='temp1',
        ),
        migrations.RemoveField(
            model_name='message',
            name='temp2',
        ),
        migrations.RemoveField(
            model_name='message',
            name='type',
        ),
        migrations.AddField(
            model_name='message',
            name='prompt',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='response',
            field=models.TextField(default=datetime.datetime(2023, 7, 28, 13, 24, 10, 976231)),
            preserve_default=False,
        ),
    ]