from django.shortcuts import render
from .models import Colacion, Almuerzos

# Create your views here.

from time import gmtime, strftime
import datetime

def index(request):
	
	return render(request,'my_chef/index.html')

def almuerzos(request):
	colaciones=Colacion.objects.all()
	diccionario={'colaciones': colaciones}
	return render(request,'my_chef/almuerzos.html',diccionario)

def reservas(request):
	colacion_id=request.POST['colacion']
	colacion=Colacion.objects.get(idcolacion=colacion_id)
	diccionario={'colacion': colacion}
	return render(request,'my_chef/reservas.html',diccionario)

def reservas_add(request):
	fecha_actual=strftime("%Y-%m-%d %H:%M:%S", gmtime())
	colacion=Colacion.objects.get(idcolacion=request.POST['colacion'])
	nombre=request.POST['nombre']
	telefono=request.POST['telefono']
	direccion=request.POST['direccion']
	opcion=request.POST['opcion']
	reserva=Almuerzos(nombre=nombre,telefono=telefono,direccion=direccion,opcion=opcion, fecha=fecha_actual)
	reserva.save()
	diccionario={'colacion':colacion, 'reserva':reserva}
	return render(request,'my_chef/reservas_add.html',diccionario)

def cenas(request):
	return render(request,'my_chef/cenas.html')

def clases(request):
	return render(request,'my_chef/clases.html')
