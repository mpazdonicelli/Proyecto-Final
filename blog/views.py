from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from blog.models import Reseña
from blog.forms import ReseñaForm

# Create your views here.

def listar_reseñas(request):
   contexto = {
       "reseñas": Reseña.objects.all(),
   }
   http_response = render(
       request=request,
       template_name='blog/lista_reseñas.html',
       context=contexto,
   )
   return http_response

def crear_reseña(request):
   if request.method == "POST":
       formulario = ReseñaForm(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           titulo = data["titulo"]
           subtitulo = data["subtitulo"]
           reseña = Reseña(titulo=titulo, subtitulo=subtitulo)  # lo crean solo en RAM
           reseña.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista de cursos
           url_exitosa = reverse('listar_reseñas')  # estudios/cursos/
           return redirect(url_exitosa)
   else:  # GET
       formulario = ReseñaForm()
   http_response = render(
       request=request,
       template_name='blog/crear_reseña.html',
       context={'formulario': formulario}
   )
   return http_response

def eliminar_reseña(request, id):
   reseña = Reseña.objects.get(id=id)
   if request.method == "POST":
       reseña.delete()
       url_exitosa = reverse('lista_reseñas')
       return redirect(url_exitosa)