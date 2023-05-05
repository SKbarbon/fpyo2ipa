import subprocess

# Run the terminal command
process = subprocess.Popen(["python3"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

# Send inputs to the command
process.stdin.write(b"""
import os

if os.environ.get('VIRTUAL_ENV') is not None:
    print("Python is running inside a virtual environment")
else:
    print("Python is not running inside a virtual environment")
""")

# Read output from the command
output, error = process.communicate()