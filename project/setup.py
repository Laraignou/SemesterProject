import sys
import subprocess
import os
import time

def Download_and_Install_Libraries():

    # implement pip as a subprocess:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',
    'numpy'])
    
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',
    'seaborn'])

    subprocess.check_call([sys.executable, '-m', 'pip', 'install',
    'pandas'])
    
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',
    'tqdm'])
    
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',
    'console-menu'])

    # subprocess.check_call([sys.executable, '-m', 'pip', 'install',
    # ''])

    # process output with an API in the subprocess module:c
    reqs = subprocess.check_output([sys.executable, '-m', 'pip',
    'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

    print(installed_packages)
    time.sleep(1)
    os.system('cls')
    time.sleep(1)
    print('File(s) executed succesfully')
    
# print(sys.path)


