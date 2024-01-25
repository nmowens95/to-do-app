from django.urls import path
from . import views

urlpatterns = [
     path('tasks', views.get_tasks, name='get_tasks'),
     path('tasks/<int:pk>/', views.get_task, name='get_task'),
     path('tasks/new/', views.post_task, name='post_task'),
     path('tasks/<int:pk>/update/', views.update_task, name='update_task'),
     path('tasks/<int:pk>/delete/', views.delete_task, name='delete_task'),
]