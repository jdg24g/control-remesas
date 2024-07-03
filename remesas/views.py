from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def index(request):
    return redirect('/admin')

def handler404(request, exception):
    return render(request, '404.html', status=404)

def home(request):
    return render(request,'index.html')
