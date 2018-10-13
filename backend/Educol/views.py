from django.shortcuts import render
from rest_framework.decorators import permission_classes
from Educol.models import *

from Educol.serializers import *
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

class EventoList(generics.ListCreateAPIView):
    serializer_class = EventoSerializer
    queryset = Evento.objects.all()

class EventoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventoSerializer
    queryset = Evento.objects.all()

class ActividadList(generics.ListCreateAPIView):
    serializer_class = ActividadSerializer
    queryset = Actividad.objects.all()

class ActividadDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ActividadSerializer
    queryset = Actividad.objects.all()

class UsuarioEventoList(generics.ListCreateAPIView):
    serializer_class = UsuarioEventoSerializer
    queryset = UsuarioEvento.objects.all()

class UsuarioEventoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsuarioEventoSerializer
    queryset = UsuarioEvento.objects.all()
