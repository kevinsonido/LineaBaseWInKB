from django.urls import include, path
from django.contrib import admin
from LineaBaseApp import views
from ProyectoLineaBase import settings
from .views import registropage,Loginpage
from django.contrib.auth import login



#direccion del las paginas web.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="Home"),
    path('lineabase', views.lineabase, name="lineabase"),
    path('vulnerabilidades', views.vulnerabilidades, name="vulnerabilidades"),
    path('reporte',views.reporte,name="reporte"),
    path('login', views.Loginpage, name="login"),
    path('registro',views.registropage,name="registro"),
    path('cerrarsesion',views.cerrarsesion,name="cerrarsesion"),
   
    path('exportar_a_csv',views.exportar_a_csv,name='exportar_a_csv'),
    path('exportar_a_excel',views.exportar_a_excel,name='exportar_a_excel'),
    path('exportar_a_excel_por_failed',views.exportar_a_excel_por_failed,name='exportar_a_excel_por_failed'),
    path('exportar_a_excel_por_passed',views.exportar_a_excel_por_passed,name='exportar_a_excel_por_passed'),
    path('controlesLineaBase',views.controlesLineaBase,name='controlesLineaBase'),

    path('cambiarvalorMinimunPasswordAge',views.cambiarvalorMinimunPasswordAge,name='cambiarvalorMinimunPasswordAge'),
    path('cambiarvalorminumpasslenght',views.cambiarvalorminumpasslenght,name='cambiarvalorminumpasslenght'),
    path('cambiarvalorlockooutduration',views.cambiartodos,name='cambiarvalorlockooutduration'),
    
    path('rollbackminimunpassage',views.rollbackminimunpassage,name='rollbackminimunpassage'),
    path('rollbackminimunpasslenght',views.rollbackminimunpasslenght,name='rollbackminimunpasslenght'),
    path('rollbacklockooutduration',views.rollbacklockooutduration,name='rollbacklockooutduration'),
    
    
    path('cambiartodos',views.cambiartodos,name='cambiartodos'),
    
]