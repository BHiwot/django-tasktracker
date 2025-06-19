from django.shortcuts import render
from .models import Task
from django.contrib.auth.decorators import login_required

# Show tasks assigned to the Logged-in user
@login_required
def task_list(request):
    tasks = Task.objects.filter(assigned_to=request.user) # Get user's tasks
    return render(request, 'tracker/task_list.html', {'tasks': tasks})
