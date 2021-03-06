# Generated by Django 3.2 on 2022-03-27 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_todo_task_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='task_state',
            field=models.CharField(blank=True, choices=[('to_do', 'TODO'), ('in_progress', 'In Progress'), ('done', 'Done')], default='in_progress', help_text='status of task', max_length=11),
        ),
    ]
