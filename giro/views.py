from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<meta name= theme-color content= #4ef542> Hello, world. You're at the polls index.")