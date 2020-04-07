from django.urls import path
from . import views

urlpatterns=[
	path('', views.index, name='index'),
	path('almuerzos/', views.almuerzos, name='almuerzos'),
	path('cenas/', views.cenas, name='cenas'),
	path('clases/', views.clases, name='clases'),
	path('reservas/',views.reservas,name='reservas'),
	path('reservas_add/',views.reservas_add,name='reservas_add'),
	path('inscripcion/',views.inscripcion,name='inscripcion'),
	path('pre_confirm/',views.pre_confirm,name='pre_confirm'),
	path('confirmacion/',views.confirmacion,name='confirmacion'),
]
