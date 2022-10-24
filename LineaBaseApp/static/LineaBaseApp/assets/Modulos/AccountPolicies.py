import os
import codecs

op= codecs.open('C:\\Users\\Kevin\\Desktop\\LineaBase WIndows\\Data\\securityoptions.txt','rb','utf-16')
temp =op.read()


#1.1.3 Ensure 'Minimum password age' is set to '1 or more day(s)'
def MinimumPasswordAge():
    t = u'MinimunPasswordAge = %s\r\n'
    if t%0 in temp:
        return 'Failed'
    for i in range(1,999):
        if t%i in temp:
            return 'Passed'

    return 'Failed'
#	1.1.4 Ensure 'Minimum password length' is set to '14 or more character(s)'
def MinimumPasswordLength():
	t = u'MinimumPasswordLength = %s\r\n'
	if t%0 in temp:
		return 'Failed'
	if t%14 in temp:
		return 'Passed'
	return 'Failed'

#1.1.2 Ensure 'Maximum password age' is set to '60 or fewer days, but not 0' 
def MaximumPasswordAge():
	t = u'MaximumPasswordAge = %s\r\n'
	if t%42 in temp:
		return 'Failed'
	for i in range(1,91):
		if t%i in temp:
			return 'Passed'
	return 'Failed'

#--

#	1.1.5 Ensure 'Password must meet complexity requirements' is set to 'Enabled' 
def PasswordComplexity():
	t = u'PasswordComplexity = %s\r\n'
	if t%0 in temp:
		return 'Failed'
	if t%1 in temp:
		return 'Passed'
	return 'Failed'

#	1.1.6 Ensure 'Store passwords using reversible encryption' is set to 'Disabled'
def ClearTextPassword():
	t = u'ClearTextPassword = %s\r\n'
	if t%0 in temp:
		return 'Passed'
	return 'Failed'
##########	1.2 Account Lockout Policy
#	1.2.1 Ensure 'Account lockout duration' is set to '15 or more minute(s)' -> check
def LockoutDuration():
	t = u'LockoutDuration = %s\r\n'
	for i in range(15,99999):
		if t%i in temp:
			return 'Passed'
	if u'LockoutDuration' in temp:
		return 'Failed'
	return 'Failed'
