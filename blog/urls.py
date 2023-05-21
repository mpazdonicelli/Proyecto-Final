from django.urls import path
from blog import views
from blog.views import listar_reseñas, crear_reseña, eliminar_reseña

urlpatterns = [
    path("lista-reseñas/", listar_reseñas, name="listar_reseñas"),
    path("crear-reseña/", crear_reseña, name="crear_reseña"),
    path('eliminar-reseña/<int:id>/', eliminar_reseña, name="eliminar_reseña"),
]