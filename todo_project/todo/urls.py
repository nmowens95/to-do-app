from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.todo, name='todo'),
    path('signup/', views.signup, name="signup")
]