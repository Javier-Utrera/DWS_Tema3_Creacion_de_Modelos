# Generated by Django 5.1.2 on 2024-10-10 11:51

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descipcion', models.TextField()),
                ('duracion_estimada', models.FloatField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_finalizacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('correo_electronico', models.CharField(max_length=30, unique=True)),
                ('contrasenia', models.CharField(max_length=30)),
                ('fecha_de_registro', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('prioridad', models.IntegerField()),
                ('estado', models.CharField(choices=[('Pend', 'Pendiente'), ('Prog', 'Progreso'), ('Comp', 'Completada')], max_length=4)),
                ('completada', models.BooleanField(default=False)),
                ('hora_vencimiento', models.TimeField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestor_Tareas.proyecto')),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestor_Tareas.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('etiquetas_asociadas', models.ManyToManyField(to='Gestor_Tareas.tarea')),
            ],
        ),
        migrations.CreateModel(
            name='Asignacion_tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observaciones', models.TextField()),
                ('fecha_asignacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestor_Tareas.tarea')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestor_Tareas.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='tarea',
            name='usuarios_asignados',
            field=models.ManyToManyField(related_name='usuarios_asignados', through='Gestor_Tareas.Asignacion_tarea', to='Gestor_Tareas.usuario'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='creador',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Gestor_Tareas.usuario'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='usuarios_asignados',
            field=models.ManyToManyField(related_name='usuarios', to='Gestor_Tareas.usuario'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_comentario', models.DateTimeField()),
                ('tarea', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Gestor_Tareas.tarea')),
                ('autor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Gestor_Tareas.usuario')),
            ],
        ),
    ]
