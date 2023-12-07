from django.shortcuts import render,HttpResponse
from .models import Cliente,Transaccion
from .controllers import sumar

# Create your views here.

def index(request):
    Transacciones = Transaccion.objects.all()
    tigo_757 = sumar.filtrar('tigo-757')
    tigo_349 = sumar.filtrar('tigo-349')
    tigo_722 = sumar.filtrar('tigo-722')
    zimple_757 = sumar.filtrar('zimple-757')
    zimple_349 = sumar.filtrar('zimple-349')
    zimple_722 = sumar.filtrar('zimple-722')
    wally_757 = sumar.filtrar('wally-757')
    wally_349 = sumar.filtrar('wally-349')
    wally_722 = sumar.filtrar('wally-722')
    interfisa = sumar.filtrar('interfisa')
    total = sumar.monto_total()
    context = {
        'Transacciones':Transacciones,
        'tigo_757':tigo_757,
        'tigo_349':tigo_349,
        'tigo_722':tigo_722,
        'zimple_757':zimple_757,
        'zimple_349':zimple_349,
        'zimple_722':zimple_722,
        'wally_757':wally_757,
        'wally_349':wally_349,
        'wally_722':wally_722,
        'interfisa':interfisa,
        'total':total,
    }
    
    return render(request,"index.html",context)