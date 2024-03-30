from django.urls import path, include
from.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', home, name = "home"),
    
    
     # __________________ Otras páginas
    path('acerca/', acerca, name="acerca_de_mi"),
    
    
    #___________________________equipos
    path('equipos', equipos, name = "equipos"),
    path('equipo_create', equipoCreate, name = "equipo_create"),
    path('equipo_update/<id_equipo>/', equipoUpdate, name = "equipo_update"),
    path('equipo_delete/<id_equipo>/', equipoDelete, name = "equipo_delete"),
    
    #___________________________equipozonados
    path('equipozonados', EquipoZonaDosList.as_view(), name = "equipozonados"),
    path('equipozonados_create', EquipoZonaDosCreate.as_view(), name = "equipozonados_create"), 
    path('equipozonados_update/<int:pk>/', EquipoZonaDosUpdate.as_view(), name = "equipozonados_update"),
    path('equipozonados_delete/<int:pk>/', EquipoZonaDosDelete.as_view(), name = "equipozonados_delete"),
    
    
    #__________________________goleadores
    path('goleadores', goleadores, name = "goleadores"),
    path('goleador_create', goleadorCreate, name = "goleador_create"),
    path('goleador_update/<id_goleador>/', goleadorUpdate, name = "goleador_update"),
    path('goleador_delete/<id_goleador>/', goleadorDelete, name = "goleador_delete"),
    
    
    #__________________________posiciones 
    path('posiciones', PosicionList.as_view(), name = "posiciones"),
    path('posicion_create', PosicionCreate.as_view(), name = "posicion_create"),   
    path('posicion_update/<int:pk>/', PosicionUpdate.as_view(), name = "posicion_update"),
    path('posicion_delete/<int:pk>/', PosicionDelete.as_view(), name = "posicion_delete"),
    
    
    #__________________________________Adicionales

    path('acerca/', acerca, name="acerca_de_mi"),



    #__________________________Busqueda
    path('buscar_equipos', buscarEquipos, name = "buscar_equipos"),
    path('encontrar_equipos', encontrarEquipos, name = "encontrar_equipos"),
    
    #____________________ Login, Logout, Registration
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html") , name="logout"),
    path('registrar/', register, name="registrar"),
    
    
     #____________________ Edicion Perfil, Cambio de Clave, Avatar
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiar_clave"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),

    
]

      
    

