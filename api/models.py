import uuid

from django.db import models
from datetime import date
from users.models import CustomUser

# Create your models here.
class Todo(models.Model):
    task_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, unique=False)
    task_title = models.CharField(max_length=200)
    task_description = models.CharField(max_length=400)

    TASK_STATUS = (
        ('to_do', 'TODO'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    )

    task_state = models.CharField(
        max_length=11,
        choices=TASK_STATUS,
        blank=True,
        default='to_do',
        help_text='status of task'
    )

    task_due_date = models.DateField(default=date.today, null=True, blank=True)

    class Meta:
        ordering = ['task_due_date']

    def __str__(self):
        return f'{self.task_title} {self.task_description} {self.task_state}'
