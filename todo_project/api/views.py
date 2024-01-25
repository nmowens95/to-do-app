# This will serialize and render out our data to json automatically
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from todo.models import Todo
from .serializers import ItemSerializer
# shortcut for error handling
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(['GET'])
def get_tasks(request):
    """
    Get all tasks
    """
    tasks = Todo.objects.all()
    serializer = ItemSerializer(tasks, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def get_task(request, pk):
    """
    Get a singular task with a given ID
    """
    task = get_object_or_404(Todo, pk=pk)
    serializer = ItemSerializer(task)
    return Response(serializer.data)

@api_view(['POST'])
def post_task(request):
    """
    Create a new task
    """
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_task(request, pk):
    """
    Update a task with the given id
    """
    try: 
        task = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response({'Error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ItemSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_task(request, pk):
    """
    Delete a task with a given ID
    """
    try:
        task = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response({'Error:':'Task not found'}, status=status.HTTP_404_NOT_FOUND)
    
    task.delete()
    return Response({'Message': 'Task deleted successfully'}, status=status.HTTP_204_NO_CONTENT)