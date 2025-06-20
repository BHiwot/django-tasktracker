from django.shortcuts import render
from .models import Task
from django.contrib.auth.decorators import login_required

# Show tasks assigned to the Logged-in user
@login_required
def task_list(request):
    try:
        tasks = Task.objects.filter(assigned_to=request.user)
        return render(request, 'tracker/task_list.html', {'tasks': tasks})
    except Exception as e:
        # Log the error 
        print("Error in task_list view:", e)

        # Show friendly error message
        return render(request, 'tracker/error.html', {'message': 'Something went wrong while loading your tasks.'})
