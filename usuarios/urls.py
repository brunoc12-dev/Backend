from django.urls import path
from .views import UsuariosHolaMundo

urlpatterns = [
    path('hola', UsuariosHolaMundo.as_view(), name='usuarios-holamundo'),
]