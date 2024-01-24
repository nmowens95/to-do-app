from rest_framework import serializers
from todo.models import Todo

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'