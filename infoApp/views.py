from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def informacion(request):
    return render(request, 'infoApp/inicio.html')