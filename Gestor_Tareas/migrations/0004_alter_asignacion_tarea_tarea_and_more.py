# Generated by Django 5.1.3 on 2024-11-18 20:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestor_Tareas', '0003_alter_etiqueta_etiquetas_asociadas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignacion_tarea',
            name='tarea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignacion_tarea_tarea', to='Gestor_Tareas.tarea'),
        ),
        migrations.AlterField(
            model_name='asignacion_tarea',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignacion_usuario', to='Gestor_Tareas.usuario'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='autor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='comentario_autor', to='Gestor_Tareas.usuario'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='tarea',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='comentario_tarea', to='Gestor_Tareas.tarea'),
        ),
        migrations.AlterField(
            model_name='etiqueta',
            name='etiquetas_asociadas',
            field=models.ManyToManyField(related_name='etiquetas_etiquetas_asociadas', to='Gestor_Tareas.tarea'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='creador',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='proyecto_creador', to='Gestor_Tareas.usuario'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='usuarios_asignados',
            field=models.ManyToManyField(related_name='proyecto_usuarios_asignados', to='Gestor_Tareas.usuario'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='creador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarea_credor', to='Gestor_Tareas.usuario'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarea_proyecto', to='Gestor_Tareas.proyecto'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='usuarios_asignados',
            field=models.ManyToManyField(related_name='tarea_usuarios_asignados', through='Gestor_Tareas.Asignacion_tarea', to='Gestor_Tareas.usuario'),
        ),
    ]
