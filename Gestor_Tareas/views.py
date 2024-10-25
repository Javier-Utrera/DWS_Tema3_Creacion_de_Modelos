from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.views.defaults import page_not_found

# Create your views here.

    #1El index html
def index(request):
    return render(request,"index.html")

    #2lista de todos los proyectos de la aplicación 
    # con sus datos correspondientes.
def todos_los_proyectos(request):
    proyectos = Proyecto.objects.prefetch_related("usuarios_asignados").select_related("creador")
    proyectos=proyectos.all()
    return render(request,"todos_proyectos.html",{'views_proyectos_mostrar':proyectos})
    
    #3todas las tareas que están asociadas a un proyecto, 
    # ordenadas por fecha de creación descendente.
def tareas_de_un_proyecto(request,id_proyecto):
    tareas = Tarea.objects.select_related("creador","proyecto").prefetch_related("usuarios_asignados")
    tareas=tareas.filter(proyecto__id=id_proyecto).order_by("fecha_creacion")
    return render(request,"tareas_de_un_proyecto.html",{'views_proyectos_mostrar_tareas':tareas})
    
    #4todos los usuarios que están asignados a una tarea 
    # ordenados por la fecha de asignación de la tarea de forma ascendente. 
def usuarios_de_una_tarea(request, id_tarea):
    tareas=Tarea.objects.get(id=id_tarea)
    usuarios=Usuario.objects.filter(name_usuarios_asignados=id_tarea).order_by("-asignacion_tarea__fecha_asignacion")
    return render(request, "usuarios_de_una_tarea.html", {'views_usuario_de_una_tarea': usuarios,'tarea':tareas})

    #5todas las tareas que tengan un texto en concreto en las 
    # observaciones a la hora de asignarlas a un usuario.
def tareas_texto_concreto(request,observacion):
    tareas=Tarea.objects.filter(asignacion_tarea__observaciones__contains=observacion)
    return render(request, "tareas_observaciones.html", {'views_tareas_observaciones': tareas})
    
    #6todos las tareas que se han creado entre dos años y el estado 
    # sea “Completada”.
def tareas_anios_completada(request,anio1,anio2):
    tareas=Tarea.objects.filter(estado="Comp",fecha_creacion__year__gte=anio1,fecha_creacion__year__lte=anio2).all()
    return render(request, "tareas_de_un_anio.html", {'views_tareas_anios_completada': tareas})
    
    #7el último usuario que ha comentado en una tarea de un proyecto en concreto.
def ultimo_usuario_comentado(request,id_proyecto):
    usuario=Usuario.objects.filter(usuario_comentario__tarea__proyecto=id_proyecto).order_by('usuario_comentario__fecha_comentario')[:1].get()
    return render(request, "ultimo_usuario.html", {'views_ultimo_usuario_comentado': usuario})
    
    #8todos los comentarios de una tarea que empiecen por la palabra que 
    # se pase en la URL y que el año del comentario sea uno en concreto.
def todos_comentarios_palabra_anio(request,anio,palabra):
    comentarios=Comentario.objects.filter(fecha_comentario__year=anio,contenido__startswith=palabra)
    return render(request, "comentarios_tarea_palabra.html",{'views_todos_comentarios_palabra_anio' : comentarios})

    #9todas las etiquetas que se han usado en todas las tareas de un proyecto.
def todas_etiquetas_proyecto(request,id_proyecto):
    etiquetas=Etiqueta.objects.filter(etiquetas_asociadas__proyecto=id_proyecto)
    return render(request, "todas_etiquetas_proyecto.html",{'views_todas_etiquetas_proyecto' : etiquetas})
    
    #10todos los usuarios que no están asignados a una tarea.
def usuarios_sin_tarea(request):
    usuarios_sin_tarea=Usuario.objects.filter(name_usuarios_asignados__isnull=True)
    return render(request, "usuarios_sin_tarea.html",{'views_usuarios_sin_tarea' : usuarios_sin_tarea})

def mi_error_400(request,exception=None):
    return render(request,"errores/400.html",None,None,400)

def mi_error_403(request,exception=None):
    return render(request,"errores/403.html",None,None,403)

def mi_error_404(request,exception=None):
    return render(request,"errores/404.html",None,None,404)

def mi_error_500(request,exception=None):
    return render(request,"errores/500.html",None,None,500)