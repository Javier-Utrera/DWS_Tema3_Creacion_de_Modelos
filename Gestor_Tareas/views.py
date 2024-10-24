from django.shortcuts import render
from .models import *

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
    proyecto=Proyecto.objects.get(id=id_proyecto)
    tareas = Tarea.objects.select_related("creador","proyecto").prefetch_related("usuarios_asignados")
    tareas=tareas.filter(proyecto=id_proyecto).order_by("titulo")
    return render(request,"tareas_de_un_proyecto.html",{'views_proyectos_mostrar_tareas':tareas})
    
    
   
    #4todos los usuarios que están asignados a una tarea 
    # ordenados por la fecha de asignación de la tarea de forma ascendente. 


 
    #5todas las tareas que tengan un texto en concreto en las 
    # observaciones a la hora de asignarlas a un usuario.
    
    #6todos las tareas que se han creado entre dos años y el estado 
    # sea “Completada”.
    
    #7el último usuario que ha comentado en una tarea de un proyecto en concreto.

    #8odos los comentarios de una tarea que empiecen por la palabra que 
    # se pase en la URL y que el año del comentario sea uno en concreto.
    
    #9todas las etiquetas que se han usado en todas las tareas de un proyecto.

    #10todos los usuarios que no están asignados a una tarea.




