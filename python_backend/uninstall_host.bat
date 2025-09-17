@echo off
set HOST_NAME=com.vikas.translator
echo Removing native messaging host: %HOST_NAME%...
REG DELETE "HKEY_CURRENT_USER\Software\Google\Chrome\NativeMessagingHosts\%HOST_NAME%" /f
echo Host has been unregistered.
pause
