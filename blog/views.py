from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from blog.models import Reseña
from blog.forms import ReseñaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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
           data = formulario.cleaned_data  
           titulo = data["titulo"]
           subtitulo = data["subtitulo"]
           cuerpo = data["cuerpo"]
           autor = data["autor"]
           fecha = data["fecha"]
           reseña = Reseña(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, fecha=fecha)  
           reseña.save()

           url_exitosa = reverse('listar_reseñas')  
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
       url_exitosa = reverse('listar_reseñas')
       return redirect(url_exitosa)
   
def editar_reseña(request, id):
    reseña = Reseña.objects.get(id=id)
    if request.method == "POST":
        formulario = ReseñaForm(request.POST, instance=reseña)

        if formulario.is_valid():
            data = formulario.cleaned_data
            reseña.titulo = data['titulo']
            reseña.subtitulo = data['subtitulo']
            reseña.cuerpo = data['cuerpo']
            reseña.autor = data['autor']
            reseña.fecha = data['fecha']
            reseña.save()

            url_exitosa = reverse('listar_reseñas')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'titulo': reseña.titulo,
            'subtitulo': reseña.subtitulo,
            'cuerpo': reseña.cuerpo,
            'autor': reseña.autor,
            'fecha': reseña.fecha
        }
        formulario = ReseñaForm(initial=inicial)
    return render(
        request=request,
        template_name='blog/crear_reseña.html',
        context={'formulario': formulario},
    )

class ReseñaDetailView(DetailView):
    model = Reseña
    success_url = reverse_lazy('lista_reseñas')
