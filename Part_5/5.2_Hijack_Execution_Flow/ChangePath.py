# Import necessary modules for file operations and registry manipulation
import os, winreg

# Function to read the 'Path' value from the registry
def readPathValue(reghive,regpath):
    reg = winreg.ConnectRegistry(None,reghive)  # Connect to the registry hive
    key = winreg.OpenKey(reg,regpath,access=winreg.KEY_READ) # Open the registry key with read access
    index = 0
    while True:
        val = winreg.EnumValue(key,index) # Enumerate through the registry values
        if val[0] == "Path":  # Check if the value is 'Path'
            return val[1]  # Return the 'Path' value
        index += 1

# Function to edit the 'Path' value in the registry
def editPathValue(reghive,regpath,targetdir):
    path = readPathValue(reghive,regpath) # Read the current 'Path' value 
    newpath = targetdir + ";" + path # Add the target directory to the existing 'Path'
    reg = winreg.ConnectRegistry(None,reghive) # Connect to the registry hive
    key = winreg.OpenKey(reg,regpath,access=winreg.KEY_SET_VALUE) # Open the registry key with write access
    winreg.SetValueEx(key,"Path",0,winreg.REG_EXPAND_SZ,newpath)  # Set the new 'Path' value in the registry
    
# Modify user path
#reghive = winreg.HKEY_CURRENT_USER
#regpath = "Environment"
targetdir = os.getcwd()

#editPathValue(reghive,regpath,targetdir)

# Modify SYSTEM path
reghive = winreg.HKEY_LOCAL_MACHINE # Set the registry hive to HKEY_LOCAL_MACHINE
regpath = "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"  # Set the registry path for the system environment
editPathValue(reghive,regpath,targetdir)  # Edit the system 'Path' value
