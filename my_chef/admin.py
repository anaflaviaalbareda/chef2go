from django.contrib import admin
from .models import *

# Register your models here.
class AlmuerzosAdmin(admin.ModelAdmin):
	list_display = ('almuerzos_id','fecha','nombre','telefono','direccion','opcion')

admin.site.register(Almuerzos,AlmuerzosAdmin)

class ColacionesAdmin(admin.ModelAdmin):
	list_display = ('idcolacion','dia')

admin.site.register(Colacion,ColacionesAdmin)

class ClasesAdmin(admin.ModelAdmin):
	list_display = ('clases_id','nombre','gratis')
	list_filter = ('gratis',)

admin.site.register(Clases,ClasesAdmin)

class InscritosClaseAdmin(admin.ModelAdmin):
	list_display = ('insc_id','nombre','telefono','email','pagado','clases')

	def clases_nombre(self, obj):
		return obj.clases.nombre

	clases_nombre.admin_order_field = 'clases__titulo'

	list_filter = ('pagado','clases__nombre',)

admin.site.register(InscritosClase,InscritosClaseAdmin)