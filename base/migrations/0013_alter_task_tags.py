# Generated by Django 3.2.15 on 2022-10-03 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_task_listno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tags',
            field=models.CharField(choices=[('Very High', 'Very High'), ('High', 'High'), ('Mid', 'Mid'), ('Low', 'Low'), ('Very Low', 'Very Low')], default='Very High', max_length=9),
        ),
    ]