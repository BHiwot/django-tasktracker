# """
# URL configuration for tasktracker project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path, include
# from django.contrib.auth import views as auth_views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('tracker.urls')),   #Include tracker URLs
#     path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'), # Login route
#     path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), #Logout route
#     path('api/', include('tracker.api_urls')),
# ]


# from django.contrib import admin
# from django.urls import path
# from tracker import views as tracker_views
# from django.contrib.auth import views as auth_views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', tracker_views.home_view, name='home'),
#     path('tasks/', tracker_views.task_list, name='task_list'),
#     path('login/', auth_views.LoginView.as_view(template_name='tracker/login.html'), name='login'),
#     path('logout/', auth_views.LoginView.as_view(template_name='tracker/login.html'), name='logout'),
# ]


from django.contrib import admin
from django.urls import path, include
from tracker import views as tracker_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tracker_views.home_view, name='home'),
    path('dashboard/', tracker_views.user_dashboard, name='dashboard'),
    # path('complete-task/<int:task_id>/', tracker_views.complete_task, name='complete-task'),
  path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('api/', include('tracker.api_urls')),
    path('tasks/', tracker_views.task_list, name='task-list'),
]
