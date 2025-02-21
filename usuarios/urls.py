from django.urls import path
from .views import UsuariosHolaMundo
from .views import UserAppView
urlpatterns = [
    path('hola', UsuariosHolaMundo.as_view(), name='usuarios-holamundo'),
    path('user', UserAppView.as_view(), name='creacion-listado-usuarios'),
]