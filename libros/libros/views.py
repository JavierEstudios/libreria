from django.shortcuts import render, get_object_or_404
from django.views import View
from libros.models import Libro

class Listado (View):
    def get(self, request):
        libros = Libro.objects.all()
        return render(request, 'libros/listado', {'libros':libros})
    
class Detalle (View):
    def get(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        return render(request, 'libros/listado', {'libro':libro})
    
class Añadir (View):
    def get():
        return 

class Modificar (View):
    def get():
        return