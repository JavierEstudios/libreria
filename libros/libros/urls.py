from django.urls import path
from .views import Listado, Detalle, Annadir, Modificar

urlpatterns = [
    path('',Listado.as_view(), name="Listado" ),
    path('book/<int:pk>', Detalle.as_view() ,name="Detalle"),
    path('add', Annadir.as_view() ,name="Annadir"),
    path('edit/<int:pk>', Modificar.as_view() ,name="Modificar"),
]