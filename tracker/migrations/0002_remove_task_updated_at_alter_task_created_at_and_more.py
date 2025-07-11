# Generated by Django 5.2.3 on 2025-07-03 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('in_progress', 'In Progress')], default='pending', max_length=20),
        ),
    ]
