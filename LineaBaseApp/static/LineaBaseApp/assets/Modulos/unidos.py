#Librerias
import os
import codecs
#***
import os
import codecs
import getpass
from sys import path
from winreg import *
import LocalPolicies 
import AccountPolicies 

import platform
import getpass
import time
import LocalPolicies
import AccountPolicies
import Contador


op= codecs.open('C:\\Users\\Kevin\\Desktop\\LineaBase WIndows\\Data\\securityoptions.txt','rb','utf-16')
tempacc =op.read()


#1.1.3 Ensure 'Minimum password age' is set to '1 or more day(s)'
def MinimumPasswordAge():
    t = u'MinimunPasswordAge = %s\r\n'
    if t%0 in tempacc:
        return 'Failed'
    for i in range(1,999):
        if t%i in tempacc:
            return 'Passed'

    return 'Failed'
#	1.1.4 Ensure 'Minimum password length' is set to '14 or more character(s)'
def MinimumPasswordLength():
	t = u'MinimumPasswordLength = %s\r\n'
	if t%0 in tempacc:
		return 'Failed'
	if t%14 in tempacc:
		return 'Passed'
	return 'Failed'

#1.1.2 Ensure 'Maximum password age' is set to '60 or fewer days, but not 0' 
def MaximumPasswordAge():
	t = u'MaximumPasswordAge = %s\r\n'
	if t%42 in tempacc:
		return 'Failed'
	for i in range(1,91):
		if t%i in tempacc:
			return 'Passed'
	return 'Failed'

#--

#	1.1.5 Ensure 'Password must meet complexity requirements' is set to 'Enabled' 
def PasswordComplexity():
	t = u'PasswordComplexity = %s\r\n'
	if t%0 in tempacc:
		return 'Failed'
	if t%1 in tempacc:
		return 'Passed'
	return 'Failed'

#	1.1.6 Ensure 'Store passwords using reversible encryption' is set to 'Disabled'
def ClearTextPassword():
	t = u'ClearTextPassword = %s\r\n'
	if t%0 in tempacc:
		return 'Passed'
	return 'Failed'
##########	1.2 Account Lockout Policy
#	1.2.1 Ensure 'Account lockout duration' is set to '15 or more minute(s)' -> check
def LockoutDuration():
	t = u'LockoutDuration = %s\r\n'
	for i in range(15,99999):
		if t%i in tempacc:
			return 'Passed'
	if u'LockoutDuration' in tempacc:
		return 'Failed'
	return 'Failed'
	
#LocalPolicies


templocal=[]


archivo= codecs.open('C:\\Users\\Kevin\\Desktop\\LineaBase WIndows\\Data\\policies.txt','rb','utf-16')
templocal =archivo.read()

#	2.2.2 Ensure 'Access this computer from the network' is set to 'Administrators'
def SeNetworkLogonRight():
	if u'SeNetworkLogonRight = *S-1-1-0,*S-1-5-32-544,*S-1-5-32-545,*S-1-5-32-551\r\n' in templocal:
		return 'Failed'
	if u'SeNetworkLogonRight = *S-1-5-32-544\r\n' in templocal:
		return 'Passed'
	return 'Failed'

#	2.2.16 Ensure 'Deny access to this computer from the network' to include 'Guests, Local account' 
def SeDenyNetworkLogonRight():
	if u'SeDenyNetworkLogonRight = *S-1-5-32-546' in templocal:
		return 'Failed'
	if u'SeDenyNetworkLogonRight = %s,*S-1-5-32-546\r\n'%getpass.getuser() in templocal:
		return 'Passed'
	return 'Failed'

#	2.2.19 Ensure 'Deny log on locally' to include 'Guests'
def SeDenyInteractiveLogonRight():
	if u'SeDenyInteractiveLogonRight = *S-1-5-32-546\r\n' in templocal:
		return 'Passed'
	return 'Failed'
#Allow log on through Remote Desktop Services
def SeRemoteInteractiveLogonRight():
	if u'SeRemoteInteractiveLogonRight = *S-1-5-32-544,*S-1-5-32-555\r\n' in templocal:
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
	if t%'14' in templocal:
		return 'Passed'
	if t%'13' in templocal or t%'12' in templocal or t%'11' in templocal or t%'10' in templocal or t%'9' in templocal or t%'8' in templocal or t%'7' in templocal or t%'6' in templocal or t%'5' in templocal:
		return 'Passed'
	return 'Failed'

#		2.3.7.7 Ensure 'Interactive logon: Smart card removal behavior' is set to 'Lock Workstation' or higher
def ScRemoveOption():
	t = u'MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\ScRemoveOption=1,"%s"\r\n'
	if t%'0' in templocal:
		return 'Failed'
	if t%'1' in templocal or t%'2' in templocal or t%'3' in templocal:
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
	
## contador	



def Fallidos():
    failed =0
    
    if(LocalPolicies.SeNetworkLogonRight()=='Failed') ==1 : failed +=1
    if(LocalPolicies.SeDenyNetworkLogonRight()=='Failed') ==1 : failed+=1
    if(LocalPolicies.SeDenyInteractiveLogonRight()=='Failed')==1 :failed+=1
    if(LocalPolicies.SeRemoteInteractiveLogonRight()=='Failed')==1 : failed+=1
    if(LocalPolicies.DontDisplayLastUserName()=='Failed')==1: failed+=1
    
    if(AccountPolicies.MinimumPasswordAge()=='Failed')==1: failed+=1
    if(AccountPolicies.MinimumPasswordLength()=='Failed')==1 : failed+=1
    if(AccountPolicies.MaximumPasswordAge()=='Failed') ==1 :failed+=1
    if (AccountPolicies.PasswordComplexity() == 'Failed') ==1 : failed+=1
    if (AccountPolicies.ClearTextPassword() == 'Failed') ==1 : failed+=1
    if (AccountPolicies.LockoutDuration() == 'Failed') ==1 : failed+=1
    if (LocalPolicies.PasswordExpiryWARNING() == 'Failed') ==1 : failed+=1
    if (LocalPolicies.ScRemoveOption() == 'Failed') ==1 : failed+=1
    if (LocalPolicies.RequireSecuritySignature() == 'Failed') ==1 :  failed+=1
    if (LocalPolicies.EnableSecuritySignature() == 'Failed') ==1 : failed+=1
    if (LocalPolicies.NullSessionPipes() == 'Failed') ==1 : failed+=1
    if (LocalPolicies.restrictnullsessaccess() == 'Failed') ==1 : failed+=1
    
    return failed


def Passed():
    passed =0 
    if(LocalPolicies.SeNetworkLogonRight()=='Passed') ==1 : passed +=1
    if(LocalPolicies.SeDenyNetworkLogonRight()=='Passed') ==1 : passed+=1
    if(LocalPolicies.SeDenyInteractiveLogonRight()=='Passed')==1 :passed+=1
    if(LocalPolicies.SeRemoteInteractiveLogonRight()=='Passed')==1 : passed+=1
    if(LocalPolicies.DontDisplayLastUserName()=='Passed')==1: passed+=1
    
    if(AccountPolicies.MinimumPasswordAge()=='Passed')==1: passed+=1
    if(AccountPolicies.MinimumPasswordLength()=='Passed')==1 : passed+=1
    if(AccountPolicies.MaximumPasswordAge()=='Passed') ==1 :passed+=1
    if (AccountPolicies.ClearTextPassword() == 'Passed') ==1 : passed+=1
    if (AccountPolicies.LockoutDuration() == 'Passed') ==1 : passed+=1
    if (LocalPolicies.PasswordExpiryWARNING() == 'Passed') ==1 : passed+=1
    if (LocalPolicies.ScRemoveOption() == 'Passed') ==1 : passed+=1
    if (LocalPolicies.RequireSecuritySignature() == 'Passed') ==1 :  passed+=1
    if (LocalPolicies.EnableSecuritySignature() == 'Passed') ==1 : passed+=1
    if (LocalPolicies.NullSessionPipes() == 'Passed') ==1 : passed+=1
    if (LocalPolicies.restrictnullsessaccess() == 'Passed') ==1 : passed+=1
       
    return passed	
	
	
	
# observaciones 


def observaciones():
    path = a = b = c = d = [0]
    if (LocalPolicies.SeNetworkLogonRight() == 'Failed') ==1 :
        path.append("Local Policies \ User Rights Assignment \ Access this computer from the network")
        a.append("(L1) Ensure 'Access this computer from the network' is set to 'Administrators'")
        b.append("&#9679; Level 1 <br /> &nbsp; &nbsp; &nbsp; &nbsp; &#9679; Level 1 + BitLocker")
        c.append("This policy setting allows other users on the network to connect to the computer and is required by various network protocols that include Server Message Block (SMB)-based protocols, NetBIOS, Common Internet File System (CIFS), and Component Object Model Plus (COM+).")
        d.append("This policy setting allows other users on the network to connect to the computer and is required by various network protocols that include Server Message Block (SMB)-based protocols, NetBIOS, Common Internet File System (CIFS), and Component Object Model Plus (COM+).")
    
    if (LocalPolicies.SeDenyNetworkLogonRight() == 'Failed') ==1:  
        path.append("Local Policies \ User Rights Assignment \ Deny access to this computer from the network")
    a.append("(L1) Ensure 'Deny access to this computer from the network' to include 'Guests, Local account'")
    b.append("&#9679; Level 1 <br /> &nbsp; &nbsp; &nbsp; &nbsp; &#9679; Level 1 + BitLocker")
    c.append("This policy setting prohibits users from connecting to a computer from across the network, which would allow users to access and potentially modify data remotely. In high security environments, there should be no need for remote users to access data on a computer. Instead, file sharing should be accomplished through the use of network servers.")
    d.append("To establish the recommended configuration via GP, set the following UI path to include Guests, Local account: Computer Configuration\\Policies\\Windows Settings\\Security Settings\\Local Policies\\User Rights Assignment\\Deny access to this computer from the network")
    
    if (LocalPolicies.SeDenyInteractiveLogonRight() == 'Failed') ==1 :  
        path.append("Local Policies \ User Rights Assignment \ Deny log on locally")
    a.append("(L1) Ensure 'Deny log on locally' to include 'Guests'")
    b.append("&#9679; Level 1 <br /> &nbsp; &nbsp; &nbsp; &nbsp; &#9679; Level 1 + BitLocker")
    c.append("This security setting determines which users are prevented from logging on at the computer. This policy setting supersedes the Allow log on locally policy setting if an account is subject to both policies. <br /> Important: If you apply this security policy to the Everyone group, no one will be able to log on locally.")
    d.append("To establish the recommended configuration via GP, set the following UI path to include Guests: Computer Configuration\\Policies\Windows Settings\\Security Settings\\Local Policies\\User Rights Assignment\\Deny log on locally")
    
    if (LocalPolicies.SeRemoteInteractiveLogonRight() == 'Failed') ==1 :
        path.append("Local Policies \ User Rights Assignment \ Allow log on through Remote Desktop Services")
    a.append("(L1) Ensure 'Allow log on through Remote Desktop Services' is set to 'Administrators, Remote Desktop Users'")
    b.append("&#9679; Level 1 <br /> &nbsp; &nbsp; &nbsp; &nbsp; &#9679; Level 1 + BitLocker")
    c.append("This policy setting determines which users or groups have the right to log on as a Terminal Services client. Remote desktop users require this user right. If your organization uses Remote Assistance as part of its help desk strategy, create a group and assign it this user right through Group Policy. If the help desk in your organization does not use Remote Assistance, assign this user right only to the Administrators group or use the restricted groups feature to ensure that no user accounts are part of the Remote Desktop Users group. <br /> Restrict this user right to the Administrators group, and possibly the Remote Desktop Users group, to prevent unwanted users from gaining access to computers on your network by means of the Remote Assistance feature.")
    d.append("To establish the recommended configuration via GP, set the following UI path to Administrators, Remote Desktop Users: Computer Configuration\\Policies\\Windows Settings\\Security Settings\\Local Policies\\User Rights Assignment\\Allow log on through Remote Desktop Services")    
    
    if (LocalPolicies.DontDisplayLastUserName() == 'Failed') ==1 :  
        path.append("Local Policies \ Security Options \ Interactive logon \ Interactive logon: Do not display last user name")
    a.append("(L1) Ensure 'Interactive logon: Do not display last user name' is set to 'Enabled'")
    b.append("&#9679; Level 1 <br /> &nbsp; &nbsp; &nbsp; &nbsp; &#9679; Level 1 + BitLocker")
    c.append("This policy setting determines whether the account name of the last user to log on to the client computers in your organization will be displayed in each computer's respective Windows logon screen. Enable this policy setting to prevent intruders from collecting account names visually from the screens of desktop or laptop computers in your organization.")
    d.append("To establish the recommended configuration via GP, set the following UI path to Enabled: Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\Security Options\Interactive logon: Do not display last user name")
    
    if (AccountPolicies.MinimumPasswordAge() == 'Failed') ==1 :  
        path.append("Account Policies \ Password Policy \ Minimum password age")
    a.append("(L1) Ensure 'Minimum password age' is set to '1 or more day(s)")
    b.append("&#9679; Level 1 <br /> &nbsp; &nbsp; &nbsp; &nbsp; &#9679; Level 1 + BitLocker")
    c.append("This policy setting determines the number of days that you must use a password before you can change it. The range of values for this policy setting is between 1 and 999 days. (You may also set the value to 0 to allow immediate password changes.) The default value for this setting is 0 days.")
    d.append("To establish the recommended configuration via GP, set the following UI path to 1 or more day(s): Computer Configuration\Policies\Windows Settings\Security Settings\Account Policies\Password Policy\Minimum password age ")
    
    if (AccountPolicies.MinimumPasswordLength() == 'Failed') ==1 :  
        path.append("Account Policies \ Password Policy \ Minimum password length")
    a.append("(L1) Ensure 'Minimum password length' is set to '14 or more character(s)")
    b.append("&#9679; Level 1 <br /> &nbsp; &nbsp; &nbsp; &nbsp; &#9679; Level 1 + BitLocker")
    c.append('''This policy setting determines the least number of characters that make up a password for a user account. There are many different theories about how to determine the best password length for an organization, but perhaps "pass phrase" is a better term than "password." In Microsoft Windows 2000 or later, pass phrases can be quite long and can include spaces. Therefore, a phrase such as "I want to drink a $5 milkshake" is a valid pass phrase; it is a considerably stronger password than an 8 or 10 character string of random numbers and letters, and yet is easier to remember. Users must be educated about the proper selection and maintenance of passwords, especially with regard to password length. ''')
    d.append("To establish the recommended configuration via GP, set the following UI path to 14 or more character(s): Computer Configuration\Policies\Windows Settings\Security Settings\Account Policies\Password Policy\Minimum password length")
    
    if (AccountPolicies.MaximumPasswordAge() == 'Failed') ==1 :  
        path.append("Local Policies \ Security Options \ Domain member \ Domain member: Maximum machine account password age ")
    a.append("(L1) Ensure 'Domain member: Maximum machine account password age' is set to '30 or fewer days, but not 0'")
    b.append("&#9679; Level 1 <br /> &nbsp; &nbsp; &nbsp; &nbsp; &#9679; Level 1 + BitLocker")
    c.append("This policy setting determines the maximum allowable age for a computer account password. By default, domain members automatically change their domain passwords every 30 days. If you increase this interval significantly so that the computers no longer change their passwords, an attacker would have more time to undertake a brute force attack against one of the computer accounts. <br /> Note: A value of 0 does not conform to the benchmark as it disables maximum password age.")
    d.append("To establish the recommended configuration via GP, set the following UI path to 30 or fewer days, but not 0: Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\Security Options\Domain member: Maximum machine account password age")    

    return path, a, b,c,d
     	