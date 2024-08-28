from django.db import models
from remesas.models import Cliente


# Create your models here.
class Tecnico(models.Model):
    nombre = models.CharField(max_length=255)
    tec_id = models.PositiveIntegerField(unique=True)

    class Meta:
        verbose_name = "Tecnico"
        verbose_name_plural = "Tecnicos"

    def __str__(self):
        return f"{self.tec_id} - {self.nombre}"


class Formulario(models.Model):
    CALIFICACIONES = [
        (1, "1 - Muy insatisfecho"),
        (2, "2 - Insatisfecho"),
        (3, "3 - Neutral"),
        (4, "4 - Satisfecho"),
        (5, "5 - Muy satisfecho"),
        (6, "6 - Sin Responder"),
    ]
    estados = [
        (1, "Pendiente"),
        (2, "Terminado"),
        (3, "Sin Respuesta")
    ]
    opciones = [(1, "Si"), (2, "No"), (3, "No Sabe")]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_incluido = models.DateField()
    agregado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    # Nuevos campos para el formulario
    tecnico_instalador = models.ForeignKey(
        Tecnico,
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        blank=True,
        verbose_name="Técnico instalador",
    )
    puntualidad = models.IntegerField(
        choices=CALIFICACIONES, verbose_name="Puntualidad"
    )
    calidad_instalacion = models.IntegerField(
        choices=CALIFICACIONES, verbose_name="Calidad de la Instalación"
    )
    explicacion_servicio = models.IntegerField(
        choices=CALIFICACIONES, verbose_name="Explicación del Servicio"
    )
    explicacion_pagos = models.BooleanField(
        verbose_name="Explicación de los Pagos", default=False
    )
    recomendaria_servicio = models.IntegerField(
        choices=opciones, verbose_name="¿Recomendaría este servicio a otros clientes?"
    )
    comentarios_adicionales = models.TextField(
        blank=True, null=True, verbose_name="Comentarios Adicionales"
    )
    cobrado = models.PositiveIntegerField(default=0,verbose_name="Valor Cobrado")
    
    copia_documento = models.BooleanField(
        verbose_name="El técnico entregó copia del Acuerdo del Usuario al Cliente",
        default=False,
    )

    estado = models.IntegerField(choices=estados, default=1)

    class Meta:
        verbose_name = "Formulario"
        verbose_name_plural = "Formularios"

    def __str__(self):
        return f"Formulario de {self.cliente} - {self.fecha_incluido}"
