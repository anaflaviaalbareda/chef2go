from django.contrib import admin
from .models import *

# Register your models here.
class AlmuerzosAdmin(admin.ModelAdmin):
	list_display = ('almuerzos_id','fecha','nombre','telefono','direccion','opcion')

admin.site.register(Almuerzos,AlmuerzosAdmin)

class ColacionesAdmin(admin.ModelAdmin):
	list_display = ('idcolacion','dia')

admin.site.register(Colacion,ColacionesAdmin)