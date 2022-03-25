import uuid

from django.db import models
from datetime import datetime
from users.models import CustomUser

# Create your models here.
class Todo(models.Model):
    task_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    task_title = models.CharField(max_length=200)
    task_description = models.CharField(max_length=400)

    TASK_STATUS = (
        ('td', 'TODO'),
        ('ip', 'In Progress'),
        ('d', 'Done'),
    )

    task_state = models.CharField(
        max_length=2,
        choices=TASK_STATUS,
        blank=True,
        default='td',
        help_text='status of task'
    )

    task_due_date = models.DateField(default=datetime.now, null=True, blank=True)

    class Meta:
        ordering = ['task_due_date']

    def __str__(self):
        return f'{self.id} {self.customer}'
