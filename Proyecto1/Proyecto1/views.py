from django.http import HttpResponse
import datetime
from django.template import Template, Context


def saludo(request): #Primera vista (view o controlador en MVC o MVT)

    docExterno  = open("C:/Users/luis Quiroga/Desktop/Django/Proyecto1/Proyecto1/plantillas/miplantilla.html") #Se abre ruta del archivo html

    plt = Template(docExterno.read()) #Crea la plantilla html creando el objeto template

    docExterno.close() #Se cierra el flujo. Siempre

    ctx = Context() #Se crea el contexto vacío porque no es dinámico.

    documento = plt.render(ctx) #Se renderiza el documento

    return HttpResponse(documento)

def despedida(request):

    return HttpResponse("Hasta luego, me voy de Django")


def dameFecha(request):

    fechaActual = datetime.datetime.now()

    documento = """<html>
    <body>
    <h2>
    Fecha y Hora actual %s
    </h2>
    </body>
    </html>""" % fechaActual


    return HttpResponse(documento)

def calculaEdad(request,agno):

    edadActual = 18
    periodo = agno - 2020
    edadFutura = edadActual + periodo
    documento = "<html><body><h2>En el año %s tendrás %s años" %(agno, edadFutura)

    return HttpResponse(documento)