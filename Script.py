import os
import subprocess
import sys
import winreg

# Get the script's directory path
script_path = os.path.dirname(os.path.abspath(__file__))

# List of required Python packages
required_python_packages = [
    "customtkinter",  # Add other packages as needed
]

# Adjust the path to the STATUS.txt file
status_path = os.path.join(script_path, '..', '..', 'Status', 'STATUS.txt')

# Check if "RUN_NPM_UPDATE" exists in STATUS.txt
try:
    with open(status_path, 'r') as file:
        status_content = file.read()
except FileNotFoundError:
    print(f"Error: STATUS.txt not found at {status_path}")
    input("Press Enter to exit...")
    exit()

if "RUN_NPM_UPDATE" in status_content:
    print("Lanos - Updating required NPM packages")
    result = subprocess.call(['npm', 'install'], cwd=script_path)
    if result != 0:
        print("Error: npm install failed.")
        input("Press Enter to exit...")
        exit()

# Adjust the path to the Default.mjs file
default_mjs_path = os.path.join(script_path, '..', 'DefScript.mjs')

# Call the Default.mjs file with Node.js
try:
    result = subprocess.call(['node', default_mjs_path])
    if result != 0:
        print("Error: Failed to execute Default.mjs.")
except FileNotFoundError:
    print(f"Error: Default.mjs not found at {default_mjs_path}")

# Pause equivalent
input("Press Enter to continue...")
