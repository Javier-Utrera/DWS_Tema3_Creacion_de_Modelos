from django.db import models
from django.conf import settings
from django.utils import timezone 
# Create your models here.

class Usuario(models.Model):
    nombre=models.TextField()
    correo_electronico=models.CharField(max_length=30,unique=True)
    contrasenia=models.CharField(max_length=30)
    fecha_de_registro=models.DateTimeField()
    
class Proyecto(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.TextField()
    duracion_estimada=models.FloatField()
    fecha_inicio=models.DateField()
    fecha_finalizacion=models.DateField()
    #
    usuarios_asignados=models.ManyToManyField(Usuario,related_name='proyecto_usuarios_asignados')
    creador=models.OneToOneField(Usuario,on_delete=models.CASCADE,related_name='proyecto_creador')

class Tarea(models.Model):
    opciones= [ 
        ("Pend","Pendiente"),
        ("Prog","Progreso"),
        ("Comp","Completada")
    ]
    titulo=models.CharField(max_length=100)
    descripcion=models.TextField()
    prioridad=models.IntegerField()
    estado=models.CharField(max_length=4,choices=opciones)
    completada=models.BooleanField(default=False)
    fecha_creacion=models.DateTimeField()
    hora_vencimiento=models.TimeField()
    #
    creador=models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name='tarea_creador')   
    proyecto=models.ForeignKey(Proyecto,on_delete=models.CASCADE,related_name='tarea_proyecto')
    usuarios_asignados=models.ManyToManyField(Usuario,through='Asignacion_tarea',related_name='tarea_usuarios_asignados')
       
    
class Etiqueta(models.Model):
    nombre=models.CharField(max_length=100, unique=True)
    #
    etiquetas_asociadas=models.ManyToManyField(Tarea,related_name='etiquetas_etiquetas_asociadas')
    
class Asignacion_tarea(models.Model):
    observaciones=models.TextField()
    fecha_asignacion=models.DateTimeField(default=timezone.now)
    #
    tarea=models.ForeignKey(Tarea,on_delete=models.CASCADE, related_name='asignacion_tarea_tarea')
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE, related_name='asignacion_usuario')
    
class Comentario(models.Model):
    contenido=models.TextField()
    fecha_comentario=models.DateTimeField()
    #
    autor=models.OneToOneField(Usuario,on_delete=models.CASCADE,related_name='comentario_autor')
    tarea=models.OneToOneField(Tarea,models.CASCADE,related_name='comentario_tarea')

    