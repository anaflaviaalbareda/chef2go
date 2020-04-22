from django.shortcuts import render
from .models import Colacion, Almuerzos, Clases, InscritosClase

# Create your views here.

from django.core.mail import send_mail
from django.conf import settings
from django.template import Context
from django.template.loader import get_template

# Librerias de tiempo

from time import gmtime, strftime
import datetime

from .forms import Contacto

def index(request):
	if request.POST:
		print("paso")
		nombre=request.POST['Nombre']
		telefono=request.POST['Telefono']
		email=request.POST['Email']
		mensaje=request.POST['Mensaje']
		asunto='contacto_web'
		contenido= 'Nombre: ' + nombre + '; Telefono: ' + telefono+ '; Email: ' + email + '; Mensaje: ' + mensaje
		email_from = settings.EMAIL_HOST_USER
		recipient_list = ['chefrasf@gmail.com',]
		send_mail( asunto, contenido, email_from, recipient_list,fail_silently = False)
		alerta='Mensaje Enviado, estamos en contacto contigo'
		dic={'alerta':alerta,'form':Contacto()}
		return render(request,'my_chef/index.html',dic)
	else:
		alerta=''
		dic={'alerta':alerta,'form':Contacto()}
		return render(request,'my_chef/index.html',dic)

def contacto(request):
	if request.POST:
		return render(request,'my_chef/contacto.html',dic)
	else:
		alerta=''
		dic={'alerta':alerta}
		return render(request,'my_chef/contacto.html',dic)

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
	clases=Clases.objects.all()
	diccionario={'clases':clases}
	return render(request,'my_chef/clases.html',diccionario)

def inscripcion(request):
	clase=Clases.objects.get(clases_id=request.POST['clase'])
	diccionario={'clase':clase}
	return render(request,'my_chef/inscripcion.html',diccionario)

def pre_confirm(request):
	clase=Clases.objects.get(clases_id=request.POST['clase'])
	nombre=request.POST['nombre']
	email=request.POST['email']
	telefono=request.POST['telefono']
	inscrito=InscritosClase(nombre=nombre,email=email,telefono=telefono,clases=clase)
	inscrito.save()

	template = get_template('my_chef/email.html')
	context = {'nombre': nombre, 'clase': clase}
	contenido = template.render(context)
	email_from = settings.EMAIL_HOST_USER
	recipient_list = [email,]
	asunto='Inscripcion a clases chef2GO'
	send_mail( asunto, contenido, email_from, recipient_list,fail_silently = False)

	diccionario={'clase':clase, 'inscripcion': inscrito}
	return render(request,'my_chef/pre_confirm.html',diccionario)

def confirmacion(request):
	return render(request,'my_chef/confirmacion.html')



