import LocalPolicies 
import AccountPolicies 


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