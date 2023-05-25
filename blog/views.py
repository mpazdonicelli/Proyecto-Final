from django.shortcuts import render, redirect, HttpResponse
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

@login_required
def crear_reseña(request):
    if request.method == "POST":
        formulario = ReseñaForm(request.POST)
        if formulario.is_valid():
            reseña= formulario.save(commit=False)
            reseña.autor=request.user
            reseña.save()
            return redirect('listar_reseñas')
        else:
            formulario=ReseñaForm()
        return render(request, 'blog/crear_reseña.html', {'formulario': formulario})

@login_required
def eliminar_reseña(request, id):
    reseña = Reseña.objects.get(id=id)
    if request.user == reseña.autor:
       if request.method == "POST":
        reseña.delete()
        url_exitosa = reverse('listar_reseñas')
        return redirect(url_exitosa)
    else:
        return HttpResponse ("No tenés permiso para eliminar esta reseña.")


@login_required   
def editar_reseña(request, id):
    reseña = Reseña.objects.get(id=id)
    if request.user == reseña.autor:
        if request.method == "POST":
            formulario = ReseñaForm(request.POST)
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
    else:
        return HttpResponse("No tenés permiso para editar esta reseña.")

class ReseñaDetailView(DetailView):
    model = Reseña
    success_url = reverse_lazy('lista_reseñas')
