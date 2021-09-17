from rest_framework import serializers
from .models import My_tutorial

class My_tutorialSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'description', 'created_at')
        model = My_tutorial