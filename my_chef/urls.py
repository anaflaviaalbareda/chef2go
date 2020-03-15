from django.urls import path
from . import views

urlpatterns=[
	path('', views.index, name='index'),
	path('almuerzos/', views.almuerzos, name='almuerzos'),
	path('cenas/', views.cenas, name='cenas'),
	path('clases/', views.clases, name='clases'),
	path('reservas/',views.reservas,name='reservas'),
	path('reservas_add/',views.reservas_add,name='reservas_add')
]