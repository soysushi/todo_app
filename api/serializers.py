from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields =  (
            'task_id',
            'task_title',
            'task_description',
            'task_state',
            'task_due_date',
            'user_id'
        )
