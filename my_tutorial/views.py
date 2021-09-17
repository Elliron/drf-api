from rest_framework import generics
from .serializers import My_tutorialSerializer
from .models import My_tutorial

class My_tutorialList(generics.ListCreateAPIView):
    queryset = My_tutorial.objects.all()
    serializer_class = My_tutorialSerializer

class My_tutorialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = My_tutorial.objects.all()
    serializer_class = My_tutorialSerializer