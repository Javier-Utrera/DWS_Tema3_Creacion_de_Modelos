from django.urls import path
from django.contrib import admin
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="urls_index"),
    path('proyectos/todos', views.todos_los_proyectos,name="urls_todos_los_proyectos"),
    path("tareas/<int:id_proyecto>",views.tareas_de_un_proyecto,name="urls_tarea_idproyecto"),
    path("usuario/<int:id_tarea>",views.usuarios_de_una_tarea,name="urls_usuario_idtarea"),
    path("tareas/observaciones/<str:observacion>",views.tareas_texto_concreto,name="urls_tareas_observaciones"),
    path("tareas/fecha/<int:anio1>/<int:anio2>",views.tareas_anios_completada,name="urls_tareas_anios_completada"),
    path("usuario/ultimocomentario/<int:id_proyecto>",views.ultimo_usuario_comentado,name="urls_ultimo_usuario_comentado")
]