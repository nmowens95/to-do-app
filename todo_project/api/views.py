# This will serialize and render out our data to json automatically
from rest_framework.response import Response
from rest_framework.decorators import api_view

from todo.models import Todo
from .serializers import ItemSerializer

# Create your views here.
@api_view(['GET'])
def getTask(request):
    tasks = Todo.objects.all()
    serializer = ItemSerializer(tasks, many=True)
    return Response(serializer.data)
    

@api_view(['POST'])
def postData(request):
    pass

@api_view(['PUT'])
def putData(request):
    pass

@api_view(['Delete'])
def deleteData(request):
    pass