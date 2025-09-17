@echo off
set HOST_NAME=com.vikas.translator
echo Registering Native Messaging host: %HOST_NAME%...
REM The path to the manifest file is the same directory as this script
set MANIFEST_PATH=%~dp0host.json
REG ADD "HKEY_CURRENT_USER\Software\Google\Chrome\NativeMessagingHosts\%HOST_NAME%" /ve /t REG_SZ /d "%MANIFEST_PATH%" /f
echo Host has been registered successfully.
pause

