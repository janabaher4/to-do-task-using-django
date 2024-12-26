# Generated by Django 5.1.4 on 2024-12-26 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
