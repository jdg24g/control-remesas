from django.db import models
from PIL import Image


# Crear una tabla que tenga número de referencia, tipo de transacción y compañía
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    celular = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50)
    ruc = models.CharField(max_length=50)


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
    ref = models.CharField(max_length=50, unique=True, blank=True)
    transaccion_img = models.ImageField(upload_to="transacciones", blank=True)

    def save(self, *args, **kwargs):
        if self.transaccion_img:
            # Obtener la extensión original del archivo
            ext = self.transaccion_img.name.split(".")[-1]

            # Cambiar el nombre del archivo al ID de la transacción con la extensión original
            self.transaccion_img.name = f"transacciones/{self.id}.{ext}"

            # Abrir la imagen y guardarla en formato JPG
            img = Image.open(self.transaccion_img.path)
            img.convert("RGB").save(self.transaccion_img.path, "JPEG")

        super().save(*args, **kwargs)
