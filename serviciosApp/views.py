import json
from pathlib import Path
from django.http import HttpResponse

def cargar_datos():
    archivo = Path(__file__).resolve().parent / "datos.json"
    with open(archivo, "r", encoding="utf-8") as archivo_json:
        return json.load(archivo_json)

def servicios(request):
    datos = cargar_datos()
    pagina = "<h1>Nuestros Servicios</h1>"
    for servicio in datos:
        pagina += f"""
            <h2>{servicio['nombre']}</h2>
            <p><strong>ID:</strong> {servicio['id']}</p>
            <p><strong>Descripción:</strong> {servicio['descripcion']}</p>
            <p><strong>Precio:</strong> ${servicio['precio']}</p>
            <p><strong>Disponibilidad:</strong> {servicio['disponibilidad']}</p>
            <hr>
        """
    pagina += '<br><a href="/">Volver al menú principal</a>'
    return HttpResponse(pagina)

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