from django.shortcuts import render
from django.db.models import Q,Prefetch
from .models import *


# Create your views here.

    #1El index html
def index(request):
    return render(request,"index.html")

    #2lista de todos los proyectos de la aplicación con sus datos correspondientes.
def todos_los_proyectos(request):
    proyectos = Proyecto.objects.select_related("creador").prefetch_related("creador",Prefetch("tarea_proyecto")).all()
    return render(request,"proyectos/todos_proyectos.html",{'views_proyectos_mostrar':proyectos})
    
    #3todas las tareas que están asociadas a un proyecto, ordenadas por fecha de creación descendente.
def tareas_de_un_proyecto(request,id_proyecto):
    tareas = (Tarea.objects.select_related("creador","proyecto").
              prefetch_related("usuarios_asignados",Prefetch("etiquetas_etiquetas_asociadas"),
                               Prefetch("asignacion_tarea_tarea"),
                               Prefetch("comentario_tarea")  
                               )
            )
    tareas = tareas.filter(proyecto=id_proyecto).order_by("-fecha_creacion").all()
    return render(request,"tareas/listar_tareas.html",{'views_tareas':tareas})
    
    #4todos los usuarios que están asignados a una tarea 
    # ordenados por la fecha de asignación de la tarea de forma ascendente. 
def usuarios_de_una_tarea(request, id_tarea):
    usuarios = (Usuario.objects.prefetch_related(
                            Prefetch("proyecto_creador"),
                            Prefetch("tarea_creador"),
                            Prefetch("tarea_usuarios_asignados"),
                            Prefetch("asignacion_usuario"),
                            Prefetch("comentario_autor"),
                               )
                        .filter(asignacion_usuario__tarea__id=id_tarea)
                        .order_by("asignacion_usuario__fecha_asignacion")
    ).all()   
    return render(request, "usuarios/listar_usuarios.html", {'views_usuarios': usuarios})

    #5todas las tareas que tengan un texto en concreto en las 
    # observaciones a la hora de asignarlas a un usuario.
def tareas_texto_concreto(request,usuario_id,observacion):
    tareas = (
        Tarea.objects.select_related("creador", "proyecto")
        .prefetch_related(
            "usuarios_asignados", 
            Prefetch("etiquetas_etiquetas_asociadas"),
            Prefetch("asignacion_tarea_tarea"), 
            Prefetch("comentario_tarea")
        )
    )

    tareas = tareas.filter(
        asignacion_tarea_tarea__observaciones__contains=observacion,
        asignacion_tarea_tarea__usuario_id=usuario_id
    ).all()   
    return render(request, "tareas/listar_tareas.html", {'views_tareas': tareas})
    
    #6todos las tareas que se han creado entre dos años y el estado 
    # sea “Completada”.
def tareas_anios_completada(request,anio1,anio2):
    tareas = (
        Tarea.objects.select_related("creador", "proyecto")
        .prefetch_related(
            "usuarios_asignados", 
            Prefetch("etiquetas_etiquetas_asociadas"),
            Prefetch("asignacion_tarea_tarea"), 
            Prefetch("comentario_tarea")
        )
    )
    tareas=tareas.filter(estado="Comp",fecha_creacion__year__gte=anio1,fecha_creacion__year__lte=anio2).all()
    return render(request, "tareas/listar_tareas.html", {'views_tareas': tareas})
    
    #7el último usuario que ha comentado en una tarea de un proyecto en concreto.
def ultimo_usuario_comentado(request,id_proyecto):
    usuarios = (Usuario.objects.prefetch_related(
                            Prefetch("proyecto_creador"),
                            Prefetch("tarea_creador"),
                            Prefetch("tarea_usuarios_asignados"),
                            Prefetch("asignacion_usuario"),
                            Prefetch("comentario_autor"),
                               ))
    usuarios=usuarios.filter(comentario_autor__tarea__proyecto=id_proyecto).order_by('comentario_autor__fecha_comentario')[:1].get()
    return render(request, "usuarios/ultimo_usuario.html", {'views_ultimo_usuario_comentado': usuarios})
    
    #8todos los comentarios de una tarea que empiecen por la palabra que 
    # se pase en la URL y que el año del comentario sea uno en concreto.
def todos_comentarios_palabra_anio(request,anio,palabra):   
    comentarios = (Comentario.objects.select_related("autor")
                  .filter(fecha_comentario__year=anio)
                  .filter(contenido__startswith=palabra)
    ).all()
    return render(request, "comentarios/comentarios_tarea_palabra.html",{'views_todos_comentarios_palabra_anio' : comentarios})

    #9todas las etiquetas que se han usado en todas las tareas de un proyecto.
def todas_etiquetas_proyecto(request,id_proyecto):
    etiquetas=Etiqueta.objects.prefetch_related("etiquetas_asociadas").filter(etiquetas_asociadas__proyecto=id_proyecto).all()
    return render(request, "etiquetas/todas_etiquetas_proyecto.html",{'views_todas_etiquetas_proyecto' : etiquetas})
    
    #10todos los usuarios que no están asignados a una tarea.
def usuarios_sin_tarea(request):
    usuarios = (Usuario.objects.prefetch_related(
                            Prefetch("proyecto_creador"),
                            Prefetch("tarea_creador"),
                            Prefetch("tarea_usuarios_asignados"),
                            Prefetch("asignacion_usuario"),
                            Prefetch("comentario_autor"),
                               ))
    usuarios=usuarios.filter(tarea_usuarios_asignados=None).all()
    return render(request, "usuarios/listar_usuarios.html",{'views_usuarios' : usuarios})

def mi_error_400(request,exception=None):
    return render(request,"errores/400.html",None,None,400)

def mi_error_403(request,exception=None):
    return render(request,"errores/403.html",None,None,403)

def mi_error_404(request,exception=None):
    return render(request,"errores/404.html",None,None,404)

def mi_error_500(request,exception=None):
    return render(request,"errores/500.html",None,None,500)