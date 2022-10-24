from xml.dom.minidom import Identified
from django.db import models

# Create your models here.

class HistorialEscaneo(models.Model):
    cliente_host= models.CharField(max_length=50)
    dire_ip=models.CharField(max_length=50)
    dire_puerto=models.CharField(max_length=50)
    vulnerabilidad=models.CharField(max_length=5000)
    fecha_scaneo=models.DateTimeField(auto_now_add=True)

    class Meta: 
        verbose_name = 'escaneo'
        verbose_name_plural ='escaneos'
        
    
    # meetodos que muestre determinado texto en el panel de administración.
    def __str__(self):
       return self.cliente_host
   
#tablas base de datos / Linea Base
   
class tb_lb_output(models.Model):
    id_lboutput = models.AutoField(primary_key=True)
    titulolb= models.TextField(max_length=4000, blank=False)
    subtitulolb = models.TextField(max_length=4000, blank=False)
    descrip1 = models.TextField(max_length=4000, blank=False)
    descrip2 =models.TextField(max_length=4000, blank=False)

    class Meta: 
        verbose_name = 'tb_lb_output'
        verbose_name_plural ='tb_lb_outputs'
        ordering=['id_lboutput']
        
        # meetodos que muestre determinado texto en el panel de administración.
    def __str__(self):
        return self.titulolb

class tb_lb_host(models.Model):
    hostid =models.AutoField(primary_key=True)
    hostip =models.CharField(max_length=20, blank=False)
    hostfqdn =models.CharField(max_length=50, blank=False)
  
# meetodos que muestre determinado texto en el panel de administración.
    def __str__(self):
        return self.hostip
#une tablas
#class tb_historial_escaneo_lb(models.Model):
 #   id_hist_esc_lb =models.AutoField(primary_key=True)
 #   host_id = models.ForeignKey(tb_lb_host,on_delete=models.CASCADE)
 #   idlb_output = models.ForeignKey(tb_lb_output,on_delete=models.CASCADE)    

class tb_estadolb(models.Model):
    idestado =models.AutoField(primary_key=True)
    estadolb =models.CharField(max_length=20, blank=False)
  
    def __str__(self):
       return self.estadolb
   
# ---------------vulnerabilides -------------------
class tb_folder(models.Model):
    idfolder = models.AutoField(primary_key=True)
    tipofolder = models.CharField(max_length=50, blank=False)
    nombrefolder=models.CharField(max_length=50, blank=False)
    
    class Meta: 
        verbose_name = 'tb_folder'
        verbose_name_plural ='tb_folders'
       # ordering=['nombrefolder']    
        # meetodos que muestre determinado texto en el panel de administración.
    def __str__(self):
        return str(self.idfolder)
        
class tb_scan(models.Model):
    idscan = models.AutoField(primary_key=True)
    tiposcan = models.CharField(max_length=100, blank=False)
    nombrescan= models.CharField(max_length=50, blank=False)
    #relacionar dos tablas
    #idfolder = models.ForeignKey(tb_folder,on_delete=models.CASCADE)

    class Meta: 
        verbose_name = 'tb_scan'
        verbose_name_plural ='tb_scans'
       # ordering=['nombrescan']      
        # meetodos que muestre determinado texto en el panel de administración.
    def __str__(self):
        return str(self.idscan)

class tb_host(models.Model):
    id_tbhost=models.AutoField(primary_key=True)
    idhost = models.CharField(max_length=50, blank=False)
    iphost = models.CharField(max_length=50, blank=False)
    fqdnhost= models.CharField(max_length=50, blank=False)
    starthost = models.CharField(max_length=50, blank=False)
    endhost = models.CharField(max_length=50, blank=False)
    oshost = models.CharField(max_length=50, blank=False)
    scan_id = models.ForeignKey(tb_scan,on_delete=models.CASCADE)
    
    class Meta: 
            verbose_name = 'tb_host'
            verbose_name_plural ='tb_hosts'
            ordering=['idhost']      
                # meetodos que muestre determinado texto en el panel de administración.
    def __str__(self):
        return self.fqdnhost 
                
class tb_scan_run(models.Model):
    idscanrun = models.AutoField(primary_key=True, blank=False)
    starscan= models.DateField(auto_now_add=True, blank=False)
    endscan = models.DateField(auto_now_add=True, blank=False)
   # id_scan = models.ForeignKey(tb_scan,on_delete=models.CASCADE)
    class Meta: 
        verbose_name = 'tb_scan_run'
        verbose_name_plural ='tb_scan_runs'
        #ordering=['starscan']       
        # meetodos que muestre determinado texto en el panel de administración.
    def __str__(self):
        return str(self.idscanrun)
    
class tb_plugin(models.Model):
    id_plugin = models.AutoField(primary_key=True)
    severidad= models.TextField(max_length=4000, blank=False)
    family = models.TextField(max_length=4000, blank=False)
    synopsis = models.TextField(max_length=4000, blank=False)
    descripcion = models.TextField(max_length=4000, blank=False)
    solution=models.TextField(max_length=4000, blank=False)
    
    class Meta: 
        verbose_name = 'tb_plugin'
        verbose_name_plural ='tb_plugins'
        ordering=['id_plugin']       
        # meetodos que muestre determinado texto en el panel de administración.
    def __str__(self):
        return self.severidad   
   
#une tablas historial_escaneo
#class  tb_historial_escaneo(models.Model):
 #   idhistorial_caneo = models.AutoField(primary_key=True)
 #   id_scan = models.ForeignKey(tb_scan,on_delete=models.CASCADE)
 #   id_host = models.ForeignKey(tb_host,on_delete=models.CASCADE)
#   id_plugin = models.ForeignKey(tb_plugin,on_delete=models.CASCADE)   
 #   id_estado =models.ForeignKey(tb_estadolb,on_delete=models.CASCADE)
 #   class Meta: 
 #       verbose_name = 'tb_historial_escaneo'
  #      verbose_name_plural ='tb_historial_escaneos'
  #      ordering=['idhistorial_caneo']       
        # meetodos que muestre determinado texto en el panel de administración.
 #       def __str__(self):
 #           return self.idhistorial_caneo 
      
class tb_output(models.Model):
    idoutput = models.AutoField(primary_key=True)
    puertooutput = models.CharField(max_length=50, blank=False)
    output = models.TextField(max_length=4000, blank=False)
   # id_historial_caneo= models.ForeignKey(tb_historial_escaneo, on_delete=models.CASCADE)
        
    class Meta: 
        verbose_name = 'tb_output'
        verbose_name_plural ='tb_outputs'
        ordering=['idoutput']    
        # meetodos que muestre determinado texto en el panel de administración.
    def __str__(self):
        return self.output   
   
class tb_usuario(models.Model):
       idusuarionuevo = models.AutoField(primary_key=True)
       nombreuser = models.CharField(max_length=50, blank=False)
       apellidouser = models.CharField(max_length=50, blank=False)
       username = models.CharField(max_length=50, blank=False)
       usermail = models.CharField(max_length=50, blank=False)
       passw = models.CharField(max_length=50, blank=False)