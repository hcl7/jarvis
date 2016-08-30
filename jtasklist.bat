nircmd.exe speak text "Current running processes are now been displayed on your screen sir."
tasklist >> %temp%\ProcessList.txt
python window.py "%temp%\ProcessList.txt" 700x200
timeout /t 1
del %temp%\ProcessList.txt