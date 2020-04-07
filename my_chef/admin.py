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
	list_display = ('insc_id','nombre','telefono','email','pagado')
	list_filter = ('pagado','clases')

admin.site.register(InscritosClase,InscritosClaseAdmin)