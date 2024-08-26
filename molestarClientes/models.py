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
    profesionalismo_tecnico = models.IntegerField(
        choices=CALIFICACIONES, verbose_name="Profesionalismo Técnico"
    )
    calidad_instalacion = models.IntegerField(
        choices=CALIFICACIONES, verbose_name="Calidad de la Instalación"
    )
    explicacion_servicio = models.IntegerField(
        choices=CALIFICACIONES, verbose_name="Explicación del Servicio"
    )
    recomendaria_servicio = models.IntegerField(
        choices=opciones, verbose_name="¿Recomendaría este servicio a otros clientes?"
    )
    comentarios_adicionales = models.TextField(
        blank=True, null=True, verbose_name="Comentarios Adicionales"
    )
    copia_documento = models.BooleanField(
        verbose_name="El técnico entregó copia del Acuerdo del Usuario al Cliente",
        default=False,
    )

    class Meta:
        verbose_name = "Formulario"
        verbose_name_plural = "Formularios"

    def __str__(self):
        return f"Formulario de {self.cliente} - {self.fecha_incluido}"
