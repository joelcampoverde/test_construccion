from django.shortcuts import render
from  django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.db.models import Q
from .models import *
from django.urls import reverse_lazy
from .forms import ClienteForm,PropiedadForm
# Create your views here.
def home(request):
    return render(request,'inicio.html')

class Cliente(ListView):
    model=Cliente
    template_name='cliente/list.html'
    context_object_name='cliente'
    paginate_by = 4
    

class Crear(CreateView):
    model=Cliente
    form_class=ClienteForm
    template_name='cliente/form.html'
    success_url=reverse_lazy('cliente')
    
class Editar(UpdateView):
    model=Cliente
    form_class=ClienteForm
    template_name='cliente/editar.html'
    success_url=reverse_lazy('cliente')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ACTUALIZAR '
        context['url_anterior'] = 'cliente'
        context['listar_url'] = 'cliente'
        return context

class Eliminar(DeleteView): 
    model = Cliente
    template_name='cliente/eliminar.html'
    success_url=reverse_lazy('cliente')
#----------------------------------------------------------------    

class Propiedad(ListView):
    model=Propiedad
    template_name='propiedad/list.html'
    context_object_name='propiedad'
    paginate_by = 4
    

class CrearPropiedad(CreateView):
    model=Propiedad
    form_class=PropiedadForm
    template_name='propiedad/form.html'
    success_url=reverse_lazy('propiedad')
    
class EditarPropiedad(UpdateView):
    model=Propiedad
    form_class=PropiedadForm
    template_name='propiedad/editar.html'
    success_url=reverse_lazy('propiedad')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ACTUALIZAR '
        context['url_anterior'] = 'cliente'
        context['listar_url'] = 'propiedad'
        return context

class EliminarPropiedad(DeleteView): 
    model = Propiedad
    template_name='propiedad/eliminar.html'
    success_url=reverse_lazy('propiedad')
