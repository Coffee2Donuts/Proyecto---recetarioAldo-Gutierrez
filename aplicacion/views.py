from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from django.http import HttpResponse
from .forms import *

# Create your views here.
#__________________________________________________Plantillas
def home(request):
    return render(request, "aplicacion/home.html")

def home2(request):
    return render(request, "aplicacion/home2.html")

def home3(request):
    return render(request, "aplicacion/home3.html")


#___________________________________________________Usuarios
def usuario(request):
    return render(request, "aplicacion/usuario.html")

def see_usuarios(request):
    contexto = {'usuarss': Usuario.objects.all()}
    return render(request, "aplicacion/see_usuarios.html", contexto)

def usuarioForm(request):
    if request.method == "POST":
        miForm = UsuarioForm(request.POST)
        if miForm.is_valid():
            usuer_nombre = miForm.cleaned_data.get("nombre")
            usuer_apellido = miForm.cleaned_data.get("apellido")
            usuer_email = miForm.cleaned_data.get("email")
            usuer = Usuario(nombre=usuer_nombre, apellido=usuer_apellido,
                                email=usuer_email,)
            usuer.save()
            return render(request, "aplicacion/home.html")
        else:    
            miForm = UsuarioForm()

    return render(request, "aplicacion/usuarioForm.html", {"form": miForm })



#_________________________________________________Chefs
def chefs(request):
    contexto = {'chefsito': Chef.objects.all()}
    return render(request, "aplicacion/chefs.html", contexto)

def see_chefs(request):
    return render(request, "aplicacion/see_chefs.html")

def chef_Form(request):
    if request.method == "POST":
        miForm = Chef_Form(request.POST)
        if miForm.is_valid():
            chef_nombre = miForm.cleaned_data.get("nombre")
            chef_apellido = miForm.cleaned_data.get("apellido")
            chef_email = miForm.cleaned_data.get("email")
            chef_especialidad = miForm.cleaned_data.get("especialidad")
            chef = Chef(nombre=chef_nombre, apellido=chef_apellido,
                                email=chef_email, especialidad=chef_especialidad)
            chef.save()
            return redirect(reverse_lazy('chefs'))

    else:    
        miForm = Chef_Form()

    return render(request, "aplicacion/chef_Form.html", {"form": miForm }) 

def updateChef(request, id_chef):
    chef = Chef.objects.get(id=id_chef)
    if request.method == "POST":
        miForm = Chef_Form(request.POST)
        if miForm.is_valid():
            chef.nombre = miForm.cleaned_data.get('nombre')
            chef.apellido = miForm.cleaned_data.get('apellido')
            chef.email = miForm.cleaned_data.get('email')
            chef.especialidad = miForm.cleaned_data.get('especialidad') 
            chef.save()
            return redirect(reverse_lazy('chefs'))   
    else:
        miForm = Chef_Form(initial={
            'nombre': chef.nombre,
            'apellido': chef.apellido,
            'email': chef.email,
            'especialidad': chef.especialidad,
        })
    return render(request, "aplicacion/chef_Form.html", {'form': miForm})

def borrarChef(request, id_chef):
    chef = Chef.objects.get(id=id_chef)
    chef.delete()
    return redirect(reverse_lazy('chefs'))


#______________________________________________________________Recetas
def ver_recetas(request):
    contexto = {'recetass': Recetas.objects.all()}
    return render(request, "aplicacion/ver_recetas.html", contexto)


def crear_recetas(request):
    contexto = {'recetas': Recetas.objects.all()}
    return render(request, "aplicacion/crear_recetas.html", contexto)

def receta_Form(request):
    if request.method == "POST":
        miForm = RecetaForm(request.POST)
        if miForm.is_valid():
            receta_nombre = miForm.cleaned_data.get("nombre")
            receta_dificultad = miForm.cleaned_data.get("dificultad")
            receta_porciones = miForm.cleaned_data.get("porciones")
            receta_ingredientes = miForm.cleaned_data.get("ingredientes")
            receta_procedimiento = miForm.cleaned_data.get("procedimiento")
            receta = Recetas(nombre=receta_nombre, dificultad=receta_dificultad, porciones=receta_porciones, ingredientes=receta_ingredientes,
                              procedimiento=receta_procedimiento)
            
            receta.save()
            return render(request, "aplicacion/home.html")

    else:    
        miForm = RecetaForm()

    return render(request, "aplicacion/recetasForm.html", {"form": miForm })


def buscar(request):
    return render(request, "aplicacion/buscar.html")


def buscarRecetas(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        find = Recetas.objects.filter(nombre__icontains=patron)
        contexto = {"recetass": find }
        return render(request, "aplicacion/ver_recetas.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")
