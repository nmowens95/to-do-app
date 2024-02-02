from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Todo

# Create your views here.
def home(request):
    return render(request, 'index.html')

def todo(request):
    todos = Todo.objects.all()
    template = loader.get_template('tasks.html')
    context = {'todos': todos}
    return HttpResponse(template.render(context, request))

def signup(request):
    form = UserCreationForm()
    return render(request, 'signup.html', {
        'form': form
    })