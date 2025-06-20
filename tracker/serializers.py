from rest_framework import serializers
from .models import Task

# Converts Task model to JSON
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'