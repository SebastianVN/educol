from django.contrib import admin
from .models import *

admin.site.register(Usuario)
admin.site.register(Evento)
admin.site.register(Actividad)
admin.site.register(UsuarioEvento)

# Register your models here.
