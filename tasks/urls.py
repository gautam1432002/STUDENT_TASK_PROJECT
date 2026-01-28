# tasks/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/tasks/', views.get_tasks, name='list'),
    path('api/add/', views.add_task, name='add'),
    # Add this new line below:
    path('api/delete/<int:task_id>/', views.delete_task, name='delete'),
]