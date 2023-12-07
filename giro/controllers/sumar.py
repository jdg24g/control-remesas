from ..models import Transaccion
from django.db.models import Sum

def filtrar(filtro:str):
    transacciones = Transaccion.objects.filter(metodo_DePago=filtro)
    total = transacciones.aggregate(Sum('monto'))['monto__sum'] or 0
    total_formatted = "{:,}".format(total).replace(',', '.')


    return total_formatted

def monto_total():
    transacciones = Transaccion.objects.all()
    total = transacciones.aggregate(Sum('monto'))['monto__sum'] or 0
    total_formatted = "{:,}".format(total).replace(',', '.')


    return total_formatted


