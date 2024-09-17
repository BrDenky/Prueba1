from django.shortcuts import render #Como estamos usando RestFramework esta función no se usa ya que esta en HTML
from rest_framework import generics #Maneja operaciones CRUD
from .models import To_do
from .serializers import To_Do_Serializer

# Create your views here.

#CRUD - Create, Read, Update, Delete

class CreateTo_Do(generics.CreateAPIView):
    queryset = To_do.objects.all()
    serializer_class = To_Do_Serializer

class ReadTo_Do(generics.ListAPIView):  #Read - List
    queryset = To_do.objects.all()
    serializer_class = To_Do_Serializer

class UpdateTo_Do(generics.RetrieveUpdateAPIView):  #Update - RetrieveUpdate
    queryset = To_do.objects.all()
    serializer_class = To_Do_Serializer

class DeleteTo_Do(generics.DestroyAPIView):     #Delete - Destroy
    queryset = To_do.objects.all()
    serializer_class = To_Do_Serializer
