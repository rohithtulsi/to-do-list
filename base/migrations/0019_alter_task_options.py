# Generated by Django 3.2.15 on 2022-10-21 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_auto_20221018_0558'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['complete', 'priority']},
        ),
    ]
