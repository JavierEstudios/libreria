from django.shortcuts import render, get_object_or_404
from django.views import View
from libros.models import Libro
from django.http import HttpResponseRedirect
from django.utils import timezone

from .forms import Formulario

class Listado (View):
    def get(self, request):
        libros = Libro.objects.all()
        return render(request, 'libros/listado.html', {'libros':libros})
    
class Detalle (View):
    def get(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        return render(request, 'libros/detalle.html', {'libro':libro})
    
class Añadir (View):
    form_class = Formulario
    initial = {'key': 'value'}
    temp = 'libros/añadir.html'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.temp, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('')
        return render(request, self.temp, {'form':form})

class Modificar (View):
    form_class = Formulario
    initial = {'key': 'value'}
    temp = 'libros/editar.html'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.temp, {'form':form})
    
    def post(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        form = self.form_class(request.POST)
        if form.is_valid():
            # edited_at = timezone.now
            return HttpResponseRedirect('book/<int:pk>')
        return render(request, self.temp, {'form':form})