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
    descipcion=models.TextField()
    duracion_estimada=models.FloatField()
    fecha_inicio=models.DateField()
    fecha_finalizacion=models.DateField()
    usuarios_asignados=models.ManyToManyField(Usuario,related_name='usuarios')
    creador=models.OneToOneField(Usuario,on_delete=models.CASCADE)

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
    hora_vencimiento=models.TimeField()
    creador=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    usuarios_asignados=models.ManyToManyField(Usuario,through='Asignacion_tarea',related_name='usuarios_asignados')
    proyecto=models.ForeignKey(Proyecto,on_delete=models.CASCADE)
    

    
    
class Etiqueta(models.Model):
    nombre=models.CharField(max_length=100, unique=True)
    etiquetas_asociadas=models.ManyToManyField(Tarea)
    
class Asignacion_tarea(models.Model):
    tarea=models.ForeignKey(Tarea,on_delete=models.CASCADE)
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    observaciones=models.TextField()
    fecha_asignacion=models.DateTimeField(default=timezone.now)
    
class Comentario(models.Model):
    autor=models.OneToOneField(Usuario,on_delete=models.CASCADE)
    tarea=models.OneToOneField(Tarea,models.CASCADE)
    contenido=models.TextField()
    fecha_comentario=models.DateTimeField()

    