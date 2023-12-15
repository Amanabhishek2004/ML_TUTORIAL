import subprocess

directory_path = r"C:\Users\AMAN\Pictures\Screenshots"

# Using 'explorer' command to open the directory in the file explorer
subprocess.Popen(['explorer', directory_path], shell=True)