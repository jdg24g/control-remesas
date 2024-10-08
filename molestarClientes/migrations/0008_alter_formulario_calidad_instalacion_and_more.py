# Generated by Django 5.0.6 on 2024-08-28 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('molestarClientes', '0007_formulario_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='calidad_instalacion',
            field=models.IntegerField(choices=[(1, '1 - Muy insatisfecho'), (2, '2 - Insatisfecho'), (3, '3 - Neutral'), (4, '4 - Satisfecho'), (5, '5 - Muy satisfecho'), (6, '6 - Sin Responder')], verbose_name='Calidad de la Instalación'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='explicacion_servicio',
            field=models.IntegerField(choices=[(1, '1 - Muy insatisfecho'), (2, '2 - Insatisfecho'), (3, '3 - Neutral'), (4, '4 - Satisfecho'), (5, '5 - Muy satisfecho'), (6, '6 - Sin Responder')], verbose_name='Explicación del Servicio'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='puntualidad',
            field=models.IntegerField(choices=[(1, '1 - Muy insatisfecho'), (2, '2 - Insatisfecho'), (3, '3 - Neutral'), (4, '4 - Satisfecho'), (5, '5 - Muy satisfecho'), (6, '6 - Sin Responder')], verbose_name='Puntualidad'),
        ),
    ]
