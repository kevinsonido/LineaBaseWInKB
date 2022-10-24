@echo off
:: BatchGotAdmin
::-------------------------------------
REM  --> Check for permissions
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params = %*:"="
    echo UAC.ShellExecute "cmd.exe", "/c %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
::--------------------------------------

::ENTER YOUR CODE BELOW:

net accounts /minpwage:35
net accounts /minpwlen:14

net accounts /lockoutduration:30

::Password Settings: Password Complexity
reg add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft Services\AdmPwd" /v PasswordComplexity /t REG_DWORD /d 4 /f
::Interactive logon: Do not display last user nam
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v dontdisplaylastusername /t REG_DWORD /d 1 /f
::Interactive logon: Prompt user to change password before expiration 5
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v PasswordExpiryWarning  /t REG_DWORD  /d 5 /f
::'Interactive logon: Smart card removal behavior valor 0
reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" /v ScRemoveOption /t REG_SZ /d 1 /f
::Microsoft network client: Digitally sign communications (always) valor default 0
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" /v RequireSecuritySignature /t REG_DWORD /d 1 /f
::Network access: Named Pipes that can be accessed anonymously
reg add "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters" /v NullSessionPipes /t REG_MULTI_SZ /d  /f