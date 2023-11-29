from django.db import models


# crear una tabla que tenga numero de referencia tipo de transaccion y compañia
class cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    celular = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50)
    ruc = models.CharField(max_length=50)


opciones_DePago = [
    ('interfisa','interfisa'),
    ('tigo-349','tigo-349'),
    ('tigo-757','tigo-757'),
    ('tigo-722','tigo-722'),
    ('zimple-349','zimple-349'),
    ('zimple-757','zimple-757'),
    ('zimple-722','zimple-722'),
    ('wally-349','wally-349'),
    ('wally-757','wally-757'),
    ('wally-722','wally-722'),


]


class transaccion(models.Model):
    metodo_DePago = models.CharField(max_length=50, choices=opciones_DePago)
    monto = models.IntegerField()
    ref = models.CharField(max_length=50, unique=True,blank=True) 
    