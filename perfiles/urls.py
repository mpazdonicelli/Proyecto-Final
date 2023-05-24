from django.urls import path
from perfiles import views
from perfiles.views import registro, login_view, CustomLogoutView, MiPerfilUpdateView, agregar_avatar, ver_perfil

urlpatterns = [
     path('signup/', registro, name="registro"),
     path('login/', login_view, name="login"),
     path('logout/', CustomLogoutView.as_view(), name="logout"),
     path('editar-mi-perfil/', MiPerfilUpdateView.as_view(), name="editar_perfil"),
     path('agregar-avatar/', agregar_avatar, name="agregar_avatar"),
     path('profile/', ver_perfil, name = ver_perfil)
     ]
