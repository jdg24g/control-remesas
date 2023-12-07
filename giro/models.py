from django.db import models


# Crear una tabla que tenga número de referencia, tipo de transacción y compañía
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    codigo_pais = models.CharField(max_length=50,blank=True)
    celular = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50)
    ruc = models.CharField(max_length=50, blank=True)

    # __str__ nombre apellido
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

opciones_DePago = [
    ("interfisa", "interfisa"),
    ("tigo-349", "tigo-349"),
    ("tigo-757", "tigo-757"),
    ("tigo-722", "tigo-722"),
    ("zimple-349", "zimple-349"),
    ("zimple-757", "zimple-757"),
    ("zimple-722", "zimple-722"),
    ("wally-349", "wally-349"),
    ("wally-757", "wally-757"),
    ("wally-722", "wally-722"),
]


class Transaccion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True)
    metodo_DePago = models.CharField(max_length=50, choices=opciones_DePago)
    monto = models.IntegerField()
    ref = models.CharField(max_length=50, blank=True)
    transaccion_img = models.ImageField("Foto", upload_to="transacciones", blank=True)
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
    editado = models.DateTimeField(auto_now=True, blank=True)
    estado = models.BooleanField("Cobrado", default=False, blank=True)

    def __str__(self) -> str:
        return f"{self.cliente}-{self.metodo_DePago}-{self.monto}"
