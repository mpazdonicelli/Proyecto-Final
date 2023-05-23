from django.urls import path
from perfiles import views
from perfiles.views import registro, login_view, CustomLogoutView, MiPerfilUpdateView

urlpatterns = [
     path('signup/', registro, name="registro"),
     path('login/', login_view, name="login"),
     path('logout/', CustomLogoutView.as_view(), name="logout"),
     path('editar-mi-perfil/', MiPerfilUpdateView.as_view(), name="editar_perfil"),
]