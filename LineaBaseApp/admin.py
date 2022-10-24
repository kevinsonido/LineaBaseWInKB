from django.contrib import admin
from .models import *



# Register your models here.
#importamos para que aparezca en administraci[on

admin.site.register(tb_lb_output)
admin.site.register(tb_lb_host)
#admin.site.register(tb_historial_escaneo_lb)

admin.site.register(tb_folder)
admin.site.register(tb_scan)
admin.site.register(tb_host)
admin.site.register(tb_scan_run)
admin.site.register(tb_plugin)
admin.site.register(tb_output)
#admin.site.register(tb_historial_escaneo)
admin.site.register(tb_estadolb)



