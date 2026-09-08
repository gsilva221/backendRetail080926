import json
from pathlib import Path
from django.http import HttpResponse
from django.shortcuts import render
def cargar_datos():
    archivo = Path(__file__).resolve().parent / "datos.json"
    with open(archivo, "r", encoding="utf-8") as archivo_json:
        return json.load(archivo_json)

def servicios(request):
    datos = cargar_datos()

    return render(request, 'servicioApp/servicios.html', {'servicios': datos})


def precios(request):
    datos = cargar_datos()  # Cargar los datos
    pagina = '''
    <h1>Precios</h1>
    <ul>
'''
    for servicio in datos:
        pagina += f'''
        <li>{servicio['nombre']}: ${servicio['precio']}</li>
'''
    pagina += '''
    </ul>
    <a href="/">Volver al menú</a>
    '''

    return HttpResponse(pagina)