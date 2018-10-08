from django.shortcuts import render
from rest_framework.decorators import permission_classes
from Educol.models import Usuario
from Educol.serializers import UsuarioSerializer
from Educol.permissions import IsPostOrIsAuthenticated
from rest_framework import generics

# Create your views here.

@permission_classes((IsPostOrIsAuthenticated, ))
class UsuarioList(generics.ListCreateAPIView):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
