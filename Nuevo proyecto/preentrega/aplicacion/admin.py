from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Equipo)
admin.site.register(Posicion)
admin.site.register(Goleador)
