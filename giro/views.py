from django.shortcuts import render,HttpResponse
from .models import Cliente,Transaccion

# Create your views here.

def index(request):
    Transacciones = Transaccion.objects.all()
    context = {
        'Transacciones':Transacciones,
    }
    return render(request,"index.html",context)