import platform
import getpass
import time
#from .LocalPolicies  import LocalPolicies 
#from .AccountPolicies import AccountPolicies 
#import Contador

def observaciones():
    path = a = b=c=d = [0]
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
     