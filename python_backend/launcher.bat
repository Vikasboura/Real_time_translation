@echo off
REM Yeh batch file Python script ko uske apne directory se chalayega.
REM %~dp0 ek special variable hai jo is batch file ki directory ko represent karta hai.
python "%~dp0native_host.py"
