#Importar clases
from random import expovariate
import sys
import os
import os.path
import shutil
import ctypes
sys.path.insert(0,'%s\Modulos'%os.getcwd())



class disable_file_system_redirection:
    _disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection
    _revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection
    def __enter__(self):
        self.old_value = ctypes.c_long()
        self.success = self._disable(ctypes.byref(self.old_value))
    def __exit__(self, type, value, traceback):
        if self.success:
            self._revert(self.old_value)
disable_file_system_redirection().__enter__()
path = r'C:\\Windows\System32\GroupPolicy\Machine\Microsoft\Windows NT\Audit\audit.csv'
if os.path.exists(path):
	shutil.copy2(path, '%s\Data'%os.getcwd())
else :
	fi = open("C:\\Users\\Kevin\\Desktop\\LineaBase WIndows\\Data\\audit.csv","r")


# importar modulo LocalPolicies
import platform
import getpass
import time
import AccountPolicies
import LocalPolicies
import Contador
#import Reportehtml


def Informaciondelsistema():
	time.sleep(0.5)
	print ('\t','_'*100,'\n')
	print ('\t\t\t\t\t','#'*25,'\n','\t\t\t\t\t##  System Infomation  ##','\n','\t\t\t\t\t','#'*25)
	print ('\t','_'*100)
	print ('\n\tOS Name :\t\t',platform.system(),platform.release(),platform.win32_ver()[2])
	print ('\tOS Version :\t\t',platform.version())
	print ('\tSystem Name :\t\t',platform.uname()[1])
	print ('\tUser Name :\t\t%s/%s'%(platform.uname()[1],getpass.getuser()))
	print ('\t','_'*100)

def AccPolicies():
    print ('\n1. Account Policies')
    print ('%s+ Minimum password age'%(' '*7),'\t\t\t\t\t[%s]'%AccountPolicies.MinimumPasswordAge())
    print ('%s+ Minimum password length'%(' '*7),'\t\t\t\t[%s]'%AccountPolicies.MinimumPasswordLength())
    print ('%s+ Maximum password age'%(' '*7),'\t\t\t\t\t[%s]'%AccountPolicies.MaximumPasswordAge())

def localpolicies():
        print ('\n2. Local Policies')
        print ('%s+ Access this computer from the network'%(' '*7),'\t\t\t\[%s]'%LocalPolicies.SeNetworkLogonRight())
        print ('%s+ Deny access to this computer from the network'%(' '*7),'\t\t\[%s]'%LocalPolicies.SeDenyNetworkLogonRight())
        print ('%s+ Deny log on locally'%(' '*7),'\t\t\t\t[%s]'%LocalPolicies.SeDenyInteractiveLogonRight())
        print ('%s+ Allow log on through Remote Desktop Services'%(' '*7),'\t\t[%s]'%LocalPolicies.SeRemoteInteractiveLogonRight())
        print ('%s* Prompt user to change password before expiration'%(' '*11),'\t\t\t[%s]'%LocalPolicies.PasswordExpiryWARNING())
        print ('%s+ Do not display last user name'%(' '*7),'\t\t\t[%s]'%LocalPolicies.DontDisplayLastUserName())
         #obtener varlo de registro
        print ('%s* Do not display last user name, con valor de registro'%(' '*11),'[%s]'%LocalPolicies.get_value_regedit_system())
        
        print ('%s* Smart card removal behavior'%(' '*11),'\t\t\t\t\t[%s]'%LocalPolicies.ScRemoveOption()) 
        print ('%s* Digitally sign communications (always)'%(' '*11),'\t\t\t\t[%s]'%LocalPolicies.RequireSecuritySignature())
        print ('%s* Digitally sign communications (if server agrees)'%(' '*11),'\t\t\t[%s]'%LocalPolicies.EnableSecuritySignature())
        print ('%s* Named Pipes that can be accessed anonymously'%(' '*11),'\t\t\t[%s]'%LocalPolicies.NullSessionPipes())
        print ('%s* Restrict anonymous access to Named Pipes and Shares'%(' '*11),'\t\t[%s]'%LocalPolicies.restrictnullsessaccess())
      
        #print ('%s* Always Install Elevated, con valor de registro'%(' '*11),'[%s]'%LocalPolicies.get_value_regedit_windows())

def Resumen():
    import types
    print ('Controles Fallidos/Aprobados')
    print ('\t\t\t|\Failed\t\t\t\t\t: %s'%Contador.Fallidos(),'\t|')
    print ('\t\t\t|\Passed\t\t\t\t\t: %s'%Contador.Passed(),'\t|')


def BenchMark():
    Informaciondelsistema()
    AccPolicies()
    localpolicies()
 
#def reporte():
  #  Reportehtml.CrearHTML()
#mostrar pantalla    
BenchMark()  
Resumen()
#reporte()


