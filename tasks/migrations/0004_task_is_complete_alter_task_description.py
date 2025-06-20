# Generated by Django 5.2.2 on 2025-06-09 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_duedate_alter_task_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
