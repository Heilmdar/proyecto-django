from django.shortcuts import render
from .models import Alumnos
from .forms import ComentarioContactoForm
from .models import ComentarioContacto
from django.shortcuts import get_object_or_404
import datetime
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages

# Create your views here.

def registros(request):
    alumnos=Alumnos.objects.all()
    return render(request, "registros/principal.html",{'alumnos':alumnos})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            comentarios = ComentarioContacto.objects.all()
            return render(request, 'registros/consultaContacto.html', {'comentarios':comentarios})
    form = ComentarioContactoForm()
    return render(request, 'registros/contacto.html',{'form': form})

def contacto(request):
    return render(request, 'registros/contacto.html')

def consultarComentarioContacto(request):
    comentarios=ComentarioContacto.objects.all()
    return render(request, 'registros/consultaContacto.html',{'comentarios':comentarios})

def eliminarComentarioContacto(request, id, confirmacion='registros/confirmarEliminacion.html'):
    comentario=get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request, 'registros/consultaContacto.html', {'comentarios':comentarios})
    return render(request, confirmacion, {'object':comentario})

def consultarComentarioIndividual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)
    return render(request,'registros/formEditarComentario.html',{'comentario':comentario})

def editarComentarioContacto(request, id):
    comentario=get_object_or_404(ComentarioContacto, id=id)
    form=ComentarioContactoForm(request.POST, instance=comentario)
    if form.is_valid():
        form.save()
        comentarios = ComentarioContacto.objects.all()
        return render(request, 'registros/consultaContacto.html', {'comentarios':comentarios})
    return render(request,'registros/formEditarComentario.html', {'comentario':comentario})


#Función filter/búsqueda d e datos
def consultar1(request):
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar2(request):
    alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar3(request):
    alumnos=Alumnos.objects.all().only("matricula", "nombre", "carrera", "turno", "imagen")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar4(request):
    alumnos=Alumnos.objects.filter(turno__contains="Vesp")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar5(request):
    alumnos=Alumnos.objects.filter(nombre__in=["Juan", "Ana"])
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar6(request):
    fechaInicio = datetime.date(2021, 7, 1)
    fechaFin = datetime.date(2021, 7, 6)
    alumnos=Alumnos.objects.filter(created__range=[fechaInicio,fechaFin])
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar7(request):
    alumnos=Alumnos.objects.filter(comentario__coment='<p>No Inscrito</p>')
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultasSQL(request):
    alumnos=Alumnos.objects.raw('SELECT id, matricula, nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')
    return render(request,"registros/consultas.html", {'alumnos':alumnos})

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion,
            archivo=archivo)
            insert.save()
            return render(request,"registros/archivos.html")
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        return render(request,"registros/archivos.html",{'archivo':Archivos})

def seguridad(request):
    return render(request,"registros/seguridad.html")

def seguridad(request, nombre=None):
    nombre = request.GET.get('nombre')
    return render(request,"registros/seguridad.html",{'nombre':nombre})