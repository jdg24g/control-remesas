from django.shortcuts import render
from remesas.models import Transaccion
from django.db.models import Sum


# Función para formatear los números como guaraníes
def format_number(number):
    if number is not None:
        return f"{number:,.0f}Gs".replace(",", ".")
    return "0Gs"


def balance_montos(request):
    # Calcula el total de todos los montos
    total_montos = Transaccion.objects.aggregate(total=Sum("monto"))["total"] or 0

    
    # Calcula el total por estado
    montos_por_estado = Transaccion.objects.values("estado").annotate(
        total=Sum("monto")
    )
    total_monto_rechazado = Transaccion.objects.filter(estado="R").aggregate(total=Sum("monto"))["total"] or 0
    total_monto_pendiente = Transaccion.objects.filter(estado="P").aggregate(total=Sum("monto"))["total"] or 0
    tot = total_monto_rechazado + total_monto_pendiente
    total_montos = total_montos - tot

    # Remplaza A por Aprobado, E por Enviado, P por Pendiente y R por Rechazado
    estado_dict = {"A": "Aprobado", "E": "Enviado", "P": "Pendiente", "R": "Rechazado"}
    for estado in montos_por_estado:
        estado["estado"] = estado_dict.get(estado["estado"], estado["estado"])
        estado["total"] = format_number(estado["total"])

    # Calcula el total por entidad
    montos_por_entidad = Transaccion.objects.values("entidad").annotate(
        total=Sum("monto")
    )
    for entidad in montos_por_entidad:
        entidad["total"] = format_number(entidad["total"])

    # Calcula el total por caja
    montos_por_caja = Transaccion.objects.values("caja").annotate(total=Sum("monto"))
    caja_dict = {"G": "Giro", "I": "Interfisa"}
    for caja in montos_por_caja:
        caja["caja"] = caja_dict.get(caja["caja"], caja["caja"])
    for caja in montos_por_caja:
        caja["total"] = format_number(caja["total"])
    # Formatear el total de montos
    total_montos = format_number(total_montos)
    context = {
        "total_montos": total_montos,
        "montos_por_estado": montos_por_estado,
        "montos_por_entidad": montos_por_entidad,
        "montos_por_caja": montos_por_caja,
    }
    return render(request, "balance.html", context)
