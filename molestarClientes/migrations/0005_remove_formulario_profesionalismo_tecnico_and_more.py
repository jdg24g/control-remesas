# Generated by Django 5.0.6 on 2024-08-28 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('molestarClientes', '0004_formulario_cobrado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formulario',
            name='profesionalismo_tecnico',
        ),
        migrations.AddField(
            model_name='formulario',
            name='explicacion_pagos',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Muy insatisfecho'), (2, '2 - Insatisfecho'), (3, '3 - Neutral'), (4, '4 - Satisfecho'), (5, '5 - Muy satisfecho')], null=True, verbose_name='Explicación de los metodos de pagos y monto abonar'),
        ),
    ]
