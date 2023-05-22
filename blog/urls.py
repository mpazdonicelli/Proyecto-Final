from django.urls import path
from blog import views
from blog.views import listar_reseñas, crear_reseña, eliminar_reseña, editar_reseña, ReseñaDetailView

urlpatterns = [
    path("lista-reseñas/", listar_reseñas, name="listar_reseñas"),
    path("crear-reseña/", crear_reseña, name="crear_reseña"),
    path('eliminar-reseña/<int:id>/', eliminar_reseña, name="eliminar_reseña"),
    path('editar-reseña/<int:id>/', editar_reseña, name="editar_reseña"),
    path('reseñas/<int:pk>/', ReseñaDetailView.as_view(), name="ver_reseña"),
]