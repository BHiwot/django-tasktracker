# from django.shortcuts import render
# from .models import Task
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse

# # ✅ New homepage view
# def home_view(request):
#     return HttpResponse("""
#         <h1>Welcome to Task Tracker 🧠</h1>
#         <p>This is your project homepage.</p>
#         <p><a href="/login/">Login</a> to manage your tasks.</p>
#     """)

# # ✅ Your existing task list view
# @login_required
# def task_list(request):
#     try:
#         tasks = Task.objects.filter(assigned_to=request.user)
#         return render(request, 'tracker/task_list.html', {'tasks': tasks})
#     except Exception as e:
#         print("Error in task_list view:", e)
#         return render(request, 'tracker/error.html', {'message': 'Something went wrong while loading your tasks.'})


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

@login_required
def home_view(request):
    return render(request, 'home.html')

@login_required
def task_list(request):
    try:
        tasks = Task.objects.filter(assigned_to=request.user)
        return render(request, 'task_list.html', {'tasks': tasks})
    except Exception as e:
        print("Error in task_list view:", e)
        return render(request, 'error.html', {'message': 'Error loading tasks.'})

# @login_required
# def complete_task(request, task_id):
#     task = get_object_or_404(Task, id=task_id, assigned_to=request.user)
#     task.completed = True
#     task.save()
#     return redirect('task-list')

@login_required
def user_dashboard(request):
    tasks = Task.objects.filter(assigned_to=request.user).order_by('-created_at')
    return render(request, 'dashboard.html', {'tasks': tasks})
