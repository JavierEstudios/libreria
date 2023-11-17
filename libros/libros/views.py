from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
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
'''

class Listado (ListView):
    model = Libro
    template_name = "libros/listado.html"

class Detalle (DetailView):
    model = Libro
    template_name = "libros/detalle.html"



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

class Modificar (View):
    template = 'libros/modificar.html'

    def get(self, request, pk):
        #libro = get_object_or_404(Libro, pk=pk)
        #form = Formulario(libro.get_deferred_fields["title","author","rating","sinopsys"])
        form = Formulario()
        return render(request, self.template, {'form':form})

    def post(self, request, pk):
        #libro = get_object_or_404(Libro, pk=pk)
        form = Formulario(request.POST)
        if form.is_valid():
            #libro.edited_at = timezone.now
            form.save()
            return redirect('book/<int:pk>')
        return render(request, self.template, {'form':form})