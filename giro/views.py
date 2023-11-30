from django.shortcuts import render,HttpResponse
from .models import Cliente,Transaccion

# Create your views here.

def index(request):
    return render(request,"index.html")