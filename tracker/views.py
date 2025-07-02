from django.shortcuts import render
from .models import Task
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# ✅ New homepage view
def home_view(request):
    return HttpResponse("""
        <h1>Welcome to Task Tracker 🧠</h1>
        <p>This is your project homepage.</p>
        <p><a href="/login/">Login</a> to manage your tasks.</p>
    """)

# ✅ Your existing task list view
@login_required
def task_list(request):
    try:
        tasks = Task.objects.filter(assigned_to=request.user)
        return render(request, 'tracker/task_list.html', {'tasks': tasks})
    except Exception as e:
        print("Error in task_list view:", e)
        return render(request, 'tracker/error.html', {'message': 'Something went wrong while loading your tasks.'})
