from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name="urls_index"),
    path('proyectos/todos', views.todos_los_proyectos,name="urls_todos_los_proyectos"),
    path("tareas/<int:id_proyecto>",views.tareas_de_un_proyecto,name="urls_tarea_idproyecto"),
    path("usuario/<int:id_tarea>",views.usuarios_de_una_tarea,name="urls_usuario_idtarea")
]