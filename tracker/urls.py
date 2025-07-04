# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home_view, name='home'),             # Fixes the 404
#     path('tasks/', views.task_list, name='task-list'),  # Lists user tasks
# ]


# tracker/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='task-list'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
]
