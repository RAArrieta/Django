from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
import datetime

def saludo(request):
    return HttpResponse("Hola Mundo...")

def con_parametros(request, apellido: str, nombre: str,):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize() 
    return HttpResponse(f"{apellido}, {nombre}")

def probando_template(request):
   
    mi_html = open("./templates/template1.html", encoding="utf-8")
    mi_template = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context()
    mi_documento = mi_template.render(mi_contexto)
    
    return HttpResponse(mi_documento)

def template_render(request):
    
    return render(request, "template2.html")

def template_render_parametros(request):
    
    nom = "Alfredo"
    ed = 42
    notas = [7,4,9,5,10]
    diccionario = {"nombre": nom, "edad": ed, "fecha": datetime.datetime.now(), "notas": notas}
    
    return render(request, "template3.html", diccionario)

def ver_personas(request):
    formulario = {
        "persona": {
            "nombre":"Alfredo",
            "edad": 42
            },
    }
    return render(request, "template4.html", formulario)
