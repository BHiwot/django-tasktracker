from django.db import models
from django.contrib.auth.models import User


# Tsk model for assigning tasks to users
class Task(models.Model):
    STATUS_CHOICES =[
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COOMPLETED', 'Completed'),
    ]

    title = models.CharField(max_length= 100) # Task title
    description = models.TextField() # Task Description
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE) #Assigned user
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default= 'PENDING') # Task Status
    created_at = models.DateTimeField(auto_created=True) # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True) #Automatically set on update

    def __str__(self):
        return self.title  # show title in admin
