import sys
import subprocess
import os
import time

def Download_and_Install_Libraries():

    print('Downloading packages if needed..')
    # implement pip as a subprocess:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',
    'numpy'])
    
    # subprocess.check_call([sys.executable, '-m', 'pip', 'install',
    # 'seaborn'])

    subprocess.check_call([sys.executable, '-m', 'pip', 'install',
    'pandas'])
    
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',
    'tqdm'])
    
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',
    'console-menu'])

    subprocess.check_call([sys.executable, '-m', 'pip', 'install',
    'scikit-learn'])

    # subprocess.check_call([sys.executable, '-m', 'pip', 'install',
    # ''])

    # process output with an API in the subprocess module:c
    reqs = subprocess.check_output([sys.executable, '-m', 'pip',
    'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

    print(installed_packages)
    os.system('cls')
    time.sleep(1)
    print('File(s) executed succesfully')

    #!/usr/bin/python



def make_directories():
# Path to be created
    # path_resources = "project/resources"
    # path_data = "project/resources/data"
    # path_database = "project/resources/database"
    # path_figures = "project/resources/figures"

    
    path_resources = "resources"
    if not os.path.exists(path_resources):
        os.mkdir(path_resources)

    path_data = "resources/data"
    if not os.path.exists(path_data):
        os.mkdir(path_data)

    path_database = "resources/database"
    if not os.path.exists(path_database):
        os.mkdir(path_database)

    path_figures = "resources/figures"
    if not os.path.exists(path_figures):
        os.mkdir(path_figures)


    print("Path is created..")


    
# print(sys.path)


