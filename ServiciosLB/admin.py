from django.contrib import admin


#llamamos la base de datos y para ejecutar pruebas manuales
#from .models import escaneo_historial
from .models import historialregistro
# Register your models here.




#class servicioadmin(admin.ModelAdmin):
 #   readonly_fields=('fecha_scaneo')

admin.site.register(historialregistro)
