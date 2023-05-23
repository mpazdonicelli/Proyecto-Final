from django.urls import path
from perfiles import views
from perfiles.views import registro, login_view, CustomLogoutView

urlpatterns = [
     path('signup/', registro, name="registro"),
     path('login/', login_view, name="login"),
     path('logout/', CustomLogoutView.as_view(), name="logout"),
]