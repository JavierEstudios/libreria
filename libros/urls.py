from django.urls import path
from .views import Listado, Detalle, Annadir, Modificar, Eliminar

urlpatterns = [
    path('',Listado.as_view(), name="Listado" ),
    path('book/<int:pk>', Detalle.as_view() ,name="Detalle"),
    path('add', Annadir.as_view() ,name="Annadir"),
    path('edit/<int:pk>', Modificar.as_view() ,name="Modificar"),
    path('delete/<int:pk>', Eliminar.as_view() ,name="Eliminar"),
]