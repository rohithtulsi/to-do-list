# Generated by Django 3.2.15 on 2022-10-30 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_remove_task_end_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='start_time',
        ),
    ]
