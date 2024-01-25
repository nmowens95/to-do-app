from django.http import HttpResponse
from django.template import loader
from .models import Todo

# Create your views here.
def todo(request):
    todos = Todo.objects.all()
    template = loader.get_template('index.html')
    context = {'todos': todos}
    return HttpResponse(template.render(context, request))