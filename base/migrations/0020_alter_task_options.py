# Generated by Django 3.2.15 on 2022-10-21 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_alter_task_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['complete']},
        ),
    ]
