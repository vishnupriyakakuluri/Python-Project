import subprocess
x = subprocess.run('dir',capture_output=True,text=True,shell=True)
print(x.stdout)
