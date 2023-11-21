from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from libros.models import Libro
from django.utils import timezone

from .forms import Formulario

'''
class Listado (View):
    def get(self, request):
        libros = Libro.objects.all()
        return render(request, 'libros/listado.html', {'libros':libros})

class Detalle (View):
    def get(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        return render(request, 'libros/detalle.html', {'libro':libro})

class Annadir (View):
    template = 'libros/annadir.html'

    def get(self, request):
        form = Formulario()
        return render(request, self.template, {'form':form})

    def post(self, request):
        form = Formulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Listado')
        return render(request, self.template, {'form':form})        
'''

class Listado (ListView):
    model = Libro
    template_name = "libros/listado.html"

class Detalle (DetailView):
    model = Libro
    template_name = "libros/detalle.html"

class Annadir (CreateView):
    model = Libro
    fields = ["title","author","rating","sinopsys"]
    template_name = 'libros/annadir.html'
    success_url = reverse_lazy("Listado")

class Modificar (UpdateView):
    model = Libro
    fields = ["title","author","rating","sinopsys"]
    template_name = 'libros/modificar.html'
    success_url = reverse_lazy("Listado")
    
class Eliminar (DeleteView):
    model = Libro
    template_name = 'libros/eliminar.html'
    success_url = reverse_lazy("Listado")