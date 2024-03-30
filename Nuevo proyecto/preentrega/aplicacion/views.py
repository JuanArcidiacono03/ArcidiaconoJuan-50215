from django.shortcuts import render, redirect 
from django.urls import reverse_lazy

from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, "aplicacion/index.html")
    
@login_required
def equipos(request):
    contexto = {'equipo': Equipo.objects.all().order_by("id")} 
    return render(request, "aplicacion/equipos.html",contexto)

@login_required
def equipozonados(request):
    contexto = {'equipo': EquipoZonaDos.objects.all().order_by("id")} 
    return render(request, "aplicacion/EquipoZonaDos.html",contexto )
 
@login_required
def goleadores(request):
    contexto = {'goleador': Goleador.objects.all()}
    return render(request, "aplicacion/goleadores.html", contexto)



#________________________________________ Adicionales
def acerca(request):
    return render(request, "aplicacion/acerca.html") 



#________________Forms
#________________Equipos

@login_required
def equipoCreate(request):
    if request.method == "POST":
        miForm = EquipoForm(request.POST)
        if miForm.is_valid():
            equipo_nombre = miForm.cleaned_data.get("nombre")
            equipo = Equipo(nombre=equipo_nombre)
            equipo.save()
            return redirect(reverse_lazy('equipos'))


    else: 
          miForm = EquipoForm() 
    return render(request, "aplicacion/equipoForm.html", {"form": miForm})

@login_required
def equipoUpdate(request , id_equipo):
    equipo = Equipo.objects.get(id=id_equipo)
    if request.method == "POST":
        miForm = EquipoForm(request.POST)
        if miForm.is_valid():
            equipo.nombre = miForm.cleaned_data.get("nombre")
            equipo.save()
            return redirect(reverse_lazy('equipos'))

    else: 
          miForm = EquipoForm(initial={'nombre':equipo.nombre}) 
    return render(request, "aplicacion/equipoForm.html", {"form": miForm})

@login_required
def equipoDelete(request, id_equipo):
    equipo = Equipo.objects.get(id=id_equipo)
    equipo.delete()
    return redirect(reverse_lazy('equipos'))


#________________Equipos


#______________________________________________________________________________________



class EquipoZonaDosList(LoginRequiredMixin, ListView):
    model = EquipoZonaDos
    
class EquipoZonaDosCreate(LoginRequiredMixin, CreateView):
    model = EquipoZonaDos
    fields = ["nombre"]
    success_url = reverse_lazy("equipozonados")
      
class EquipoZonaDosUpdate(LoginRequiredMixin, UpdateView):
    model = EquipoZonaDos
    fields = ["nombre"]
    success_url = reverse_lazy("equipozonados")
    
class EquipoZonaDosDelete(LoginRequiredMixin, DeleteView):
    model = EquipoZonaDos
    success_url = reverse_lazy("equipozonados")


#__________________________Create/Update Goleador

@login_required
def goleadorCreate(request):
    if request.method == "POST":
        miForm = GoleadorForm(request.POST)
        if miForm.is_valid():
            goleador_nombre = miForm.cleaned_data.get("nombre")
            goleador_apellido = miForm.cleaned_data.get("apellido")
            
            goleador = Goleador(nombre=goleador_nombre, apellido = goleador_apellido)
                                
            goleador.save()
           
            return redirect(reverse_lazy('goleadores'))

    else: 
          miForm = GoleadorForm() 
    return render(request, "aplicacion/goleadorForm.html", {"form": miForm})

@login_required
def goleadorUpdate(request, id_goleador):
    goleador = Goleador.objects.get(id=id_goleador)
    if request.method == "POST":
        miForm = GoleadorForm(request.POST)
        if miForm.is_valid():
            goleador.nombre = miForm.cleaned_data.get("nombre") 
            goleador.apellido = miForm.cleaned_data.get("apellido")  
            goleador.save()
            return redirect(reverse_lazy('goleadores'))


    else: 
          miForm = EquipoForm(initial={'nombre': goleador.nombre ,'apellido': goleador.apellido,}) 
    return render(request, "aplicacion/goleadorForm.html", {"form": miForm})

@login_required
def goleadorDelete(request, id_goleador):
    goleador = Goleador.objects.get(id=id_goleador)
    goleador.delete()
    return redirect(reverse_lazy('goleadores'))




#_____________________________Busqueda

@login_required
def buscarEquipos(request):
    return render(request, "aplicacion/buscar.html")

@login_required
def encontrarEquipos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        equipos = Equipo.objects.filter(nombre__icontains=patron)
        contexto = {"equipos": equipos}
        return render(request, "aplicacion/equipos.html", contexto)
    

    contexto = {'equipos': Equipo.objects.all()}
    return render(request, "aplicacion/equipos.html", contexto) 


#_____________________________Posiciones
 
class PosicionList(LoginRequiredMixin, ListView):
    model = Posicion
    
class PosicionCreate(LoginRequiredMixin, CreateView):
    model = Posicion
    fields = ["nombre"]
    success_url = reverse_lazy("posiciones")
      
class PosicionUpdate(LoginRequiredMixin, UpdateView):
    model = Posicion
    fields = ["nombre"]
    success_url = reverse_lazy("posiciones")
    
class PosicionDelete(LoginRequiredMixin, DeleteView):
    model = Posicion
    success_url = reverse_lazy("posiciones")
    
    #_____________________________Login, Logout, Authentication, Registration 
    
def login_request(request):
    if request.method == "POST":
        usuario = request.POST ['username']
        clave = request.POST ['password']
        user = authenticate(request, username=usuario , password= clave)
        if user is not None:
            login(request, user)
            
            #______ Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar

            #________________________________________________________

            
            return render (request, "aplicacion/index.html")
        else: 
            return redirect(reverse_lazy('login'))
        


    else: 
          miForm = AuthenticationForm() 
    return render(request, "aplicacion/login.html", {"form": miForm})


def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)

        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = RegistroForm()

    return render(request, "aplicacion/registro.html", {"form": miForm} )    

 #_____________________________Edicion de perfil, Cambio de contraseña y Avatars
 
@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy('home'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = UserEditForm(instance=usuario)

    return render(request, "aplicacion/editarPerfil.html", {"form": miForm} )    

   
class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "aplicacion/cambiar_clave.html"
    success_url = reverse_lazy("home")
    
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)

        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            #___ Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #____________________________________________________
            avatar = Avatar(user=usuario,
                            imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy('home'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = AvatarForm()

    return render(request, "aplicacion/agregarAvatar.html", {"form": miForm} )       
   
   
   
    
    
