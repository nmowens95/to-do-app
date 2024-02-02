from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('/', views.home, name='home'),
    path('tasks/', views.todo, name='todo'),
    path('signup/', views.signup, name="signup")
]