import os
import codecs
import getpass
from sys import path

from winreg import *


temp=[]


archivo= codecs.open('C:\\Users\\Kevin\\Desktop\\LineaBase WIndows\\Data\\policies.txt','rb','utf-16')
temp =archivo.read()

#	2.2.2 Ensure 'Access this computer from the network' is set to 'Administrators'
def SeNetworkLogonRight():
	if u'SeNetworkLogonRight = *S-1-1-0,*S-1-5-32-544,*S-1-5-32-545,*S-1-5-32-551\r\n' in temp:
		return 'Failed'
	if u'SeNetworkLogonRight = *S-1-5-32-544\r\n' in temp:
		return 'Passed'
	return 'Failed'

#	2.2.16 Ensure 'Deny access to this computer from the network' to include 'Guests, Local account' 
def SeDenyNetworkLogonRight():
	if u'SeDenyNetworkLogonRight = *S-1-5-32-546' in temp:
		return 'Failed'
	if u'SeDenyNetworkLogonRight = %s,*S-1-5-32-546\r\n'%getpass.getuser() in temp:
		return 'Passed'
	return 'Failed'

#	2.2.19 Ensure 'Deny log on locally' to include 'Guests'
def SeDenyInteractiveLogonRight():
	if u'SeDenyInteractiveLogonRight = *S-1-5-32-546\r\n' in temp:
		return 'Passed'
	return 'Failed'
#Allow log on through Remote Desktop Services
def SeRemoteInteractiveLogonRight():
	if u'SeRemoteInteractiveLogonRight = *S-1-5-32-544,*S-1-5-32-555\r\n' in temp:
		return 'Passed'
	return 'Failed'


#Opciones de seguridad regidit

def DontDisplayLastUserName():
	try: 
		key = OpenKey(HKEY_LOCAL_MACHINE, r'Software\Microsoft\Windows\CurrentVersion\Policies\System', 0, KEY_READ)
		value = (QueryValueEx(key,'DontDisplayLastUserName')[0])            
	except:
		return "Failed"
	if value == 0 :
		return 'Failed'
	if value == 1 :
		return 'Passed'
	return 'Failed'
	CloseKey(key)

 #		2.3.7.6 Ensure 'Interactive logon: Prompt user to change password before expiration' is set to 'between 5 and 14 days'
def PasswordExpiryWARNING():
	t = u'MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\PasswordExpiryWARNING=4,%s\r\n'
	if t%'14' in temp:
		return 'Passed'
	if t%'13' in temp or t%'12' in temp or t%'11' in temp or t%'10' in temp or t%'9' in temp or t%'8' in temp or t%'7' in temp or t%'6' in temp or t%'5' in temp:
		return 'Passed'
	return 'Failed'

#		2.3.7.7 Ensure 'Interactive logon: Smart card removal behavior' is set to 'Lock Workstation' or higher
def ScRemoveOption():
	t = u'MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\ScRemoveOption=1,"%s"\r\n'
	if t%'0' in temp:
		return 'Failed'
	if t%'1' in temp or t%'2' in temp or t%'3' in temp:
		return 'Passed'
	return 'Failed'

#	2.3.8 Microsoft network client
#		2.3.8.1 Ensure 'Microsoft network client: Digitally sign communications (always)' is set to 'Enabled'
def RequireSecuritySignature():
	try: 
		key = OpenKey(HKEY_LOCAL_MACHINE, r'System\CurrentControlSet\Services\LanmanWorkstation\Parameters', 0, KEY_READ)
		value = (QueryValueEx(key,'RequireSecuritySignature')[0])
	except:
		return 'Failed'
	if value == 0 :
		return 'Failed'
	if value == 1 :
		return 'Passed'
	return 'Failed'
	CloseKey(key)
#		2.3.8.2 Ensure 'Microsoft network client: Digitally sign communications (if server agrees)' is set to 'Enabled'
def EnableSecuritySignature():
	try: 
		key = OpenKey(HKEY_LOCAL_MACHINE, r'System\CurrentControlSet\Services\LanmanWorkstation\Parameters', 0, KEY_READ)
		value = (QueryValueEx(key,'EnableSecuritySignature')[0])
	except:
		return 'Failed'
	if value == 1 :
		return 'Passed'
	return 'Failed'
	CloseKey(key)

#		2.3.10.6 Ensure 'Network access: Named Pipes that can be accessed anonymously' is set to 'None' 
def NullSessionPipes():
	try: 
		key = OpenKey(HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Services\LanManServer\Parameters', 0, KEY_READ)
		value = (QueryValueEx(key,'NullSessionPipes')[0])
	except:
		return 'Failed'
	t = [u'<blank>']
	if (value == t) == 1:
		return 'Passed'
	return 'Failed'
	CloseKey(key)

#		2.3.10.9 Ensure 'Network access: Restrict anonymous access to Named Pipes and Shares' is set to 'Enabled'
def restrictnullsessaccess():
	try: 
		key = OpenKey(HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Services\LanManServer\Parameters', 0, KEY_READ)
		value = (QueryValueEx(key,'restrictnullsessaccess')[0])
	except:
		return 'Failed'
	if value == 1:
		return 'Passed'
	return 'Failed'
	CloseKey(key)

#def leer_registro(k="DontDisplayLastUserName"):
  #  try:
 #       key = OpenKeyEx(HKEY_LOCAL_MACHINE,r'Software\Microsoft\Windows\CurrentVersion\Policies\System')
 #       valor = QueryValueEx(key,k)
#        if key:
#            return 1
 #   except Exception as e:
##        print (e)

#        return 0



def get_value_regedit_windows():
    key = OpenKey(HKEY_LOCAL_MACHINE, r'Software\Policies\Microsoft\Windows\Installer')
    for i in range(100):
        try:
             
             n,v,c  = EnumValue(key,i)
             print (i,"-",n,":",v,":") 
            # if i== 15: 
             #print (i,"-",n,":",v,":")
                #return (v)   
               # return (v)
        except:
            break;
    CloseKey(key)


def get_value_regedit_system():
    key = OpenKey(HKEY_LOCAL_MACHINE, r'Software\Microsoft\Windows\CurrentVersion\Policies\System')
    for i in range(100):
        try:
             
             n,v,c  = EnumValue(key,i)
             #print (i,"-",n,":",v,":") 
             if i== 15: 
             #print (i,"-",n,":",v,":")
                #return (v)   
                return (v)
        except:
            break;
    CloseKey(key)
    

##########	19.1 Control Panel
#	19.1.1 Add or Remove Programs
#	19.1.2 Display
#	19.1.3 Personalization
#		19.1.3.1 Ensure 'Enable screen saver' is set to 'Enabled'

def get_user_sid():
	username = "%s"%getpass.getuser()
	b = "wmic useraccount where name='%s' get sid"%username
	sid= os.popen(b).read()
	return sid.split()[1]

def ScreenSaveActive():
	try: 
		key = OpenKey(HKEY_USERS, r'%s\Software\Policies\Microsoft\Windows\Control Panel\Desktop'%get_user_sid(), 0, KEY_ALL_ACCESS)
		value = int(QueryValueEx(key,'ScreenSaveActive')[0])
	except:
		return "Failed"
	if value == 1 :
		return 'Passed'
	return 'Failed';
	CloseKey(key)
	
#		19.1.3.2 Ensure 'Force specific screen saver: Screen saver executable name' is set to 'Enabled: scrnsave.scr'	
def SCRNSAVE():
	try: 
		key = OpenKey(HKEY_USERS, r'%s\Software\Policies\Microsoft\Windows\Control Panel\Desktop'%get_user_sid(), 0, KEY_ALL_ACCESS)
		value = (QueryValueEx(key,'SCRNSAVE.EXE')[0])
	except:
		return "Failed"
	temp = 'scrnsave.scr'
	if (value == temp) == 1 :
		return 'Passed'
	return 'Failed';
	CloseKey(key)
	
#		19.1.3.3 Ensure 'Password protect the screen saver' is set to 'Enabled'
def ScreenSaverIsSecure():
	try: 
		key = OpenKey(HKEY_USERS, r'%s\Software\Policies\Microsoft\Windows\Control Panel\Desktop'%get_user_sid(), 0, KEY_ALL_ACCESS)
		value = int(QueryValueEx(key,'ScreenSaverIsSecure')[0])
	except:
		return "Failed"
	if value == 1 :
		return 'Passed'
	return 'Failed';
	CloseKey(key)
	
#		19.1.3.4 Ensure 'Screen saver timeout' is set to 'Enabled: 900 seconds or fewer, but not 0'
def ScreenSaveTimeOut():
	try: 
		key = OpenKey(HKEY_USERS, r'%s\Software\Policies\Microsoft\Windows\Control Panel\Desktop'%get_user_sid(), 0, KEY_ALL_ACCESS)
		value = int(QueryValueEx(key,'ScreenSaveTimeOut')[0])
	except:
		return "Failed"
	if value <= 900 and value > 0 :
		return 'Passed'
	elif value == 0:
		return "Failed"
	return 'Failed';
	CloseKey(key)
 
def AlwaysInstallElevated():
	try: 
		key = OpenKey(HKEY_USERS, r'%s\Software\Policies\Microsoft\Windows\Installer'%get_user_sid(), 0, KEY_ALL_ACCESS)
		value = (QueryValueEx(key,'AlwaysInstallElevated')[0])
	except:
		return "Failed"
	if value == 0:
		return 'Passed'
	return 'Failed';
	CloseKey(key)

#		19.7.41.2.1 Ensure 'Prevent Codec Download' is set to 'Enabled'
def PreventCodecDownload():
	try: 
		key = OpenKey(HKEY_USERS, r'%s\Software\Policies\Microsoft\WindowsMediaPlayer'%get_user_sid(), 0, KEY_ALL_ACCESS)
		value = (QueryValueEx(key,'PreventCodecDownload')[0])
	except:
		return "Failed"
	if value == 1:
		return 'Passed'
	return 'Failed';
	CloseKey(key)
	