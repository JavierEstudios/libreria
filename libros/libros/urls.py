from django.urls import path
from .views import Listado, Detalle, Añadir, Modificar

urlpatterns = [
    path('',Listado.as_view(), name="ListadoLibros" ),
    path('book/<int:pk>', Detalle.as_view() ,name="DetalleLibro"),
    path('add', Añadir.as_view() ,name="AñadeLibro"),
    path('edit/<int:pk>', Modificar.as_view() ,name="EditaLibro"),
]