from django.shortcuts import render
from django.contrib import messages
from .models import Materia, Grado, Asignacion
from .forms import GradoForm

def asignacion_nueva(request):
    if request.method == "POST":
        formulario = GradoForm(request.POST)
        if formulario.is_valid():
            grado = Grado.objects.create(nombre=formulario.cleaned_data['nombre'], seccion = formulario.cleaned_data['seccion'])
            for materia_id in request.POST.getlist('materias'):
                asignacion = Asignacion(materia_id=materia_id, grado_id = grado.id)
                asignacion.save()
            messages.add_message(request, messages.SUCCESS, 'Asignacion exitosa')
    else:
        formulario = GradoForm()
    return render(request, 'colegio/crear_asignacion.html', {'formulario': formulario})
