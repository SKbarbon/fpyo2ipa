from .the_app_py import The_app_py_script
from .the_localhost_py import The_localhost_py_script
from ..Tools.unzip_assets import Unzip_asset
import os
import shutil
import subprocess
import sys

def edit_an_exist_project():
    print("Create a briefcase project..")
    Unzip_asset()

    project_name = "pyo2ipadist"
    if not os.path.isdir(project_name):
        raise FileNotFoundError(f"There is no folder with path '{project_name}'.")
    
    if not os.path.isdir(f"{project_name}/src"):
        raise FileNotFoundError(f"There is no folder with path '{project_name}/src'.")
    
    if not os.path.isdir(f"{project_name}/src/pyo2ipadist/assets"):
        os.mkdir(f"{project_name}/src/pyo2ipadist/assets")
    
    if not os.path.isdir("dist"):
        raise FileNotFoundError("There must be a flet-pyodide folder called `dist` to start.")
    
    print("editing the dist..")
    if '  <base href="/basedurlhere/">' in open("dist/index.html", encoding="utf-8").read():
        pass
    elif '  <base href="/">' not in open("dist/index.html", encoding="utf-8").read():
        sys.exit("Exit with Error: The base/href url of the dist must be '/'.")
    
    the_index_file = open("dist/index.html", encoding="utf-8").read()
    the_index_file = str(the_index_file).replace('  <base href="/">', '  <base href="/basedurlhere/">')
    open("dist/index.html", "w+", encoding="utf-8").write(the_index_file)
    
    print("copy the dist..")
    if os.path.isdir(f"{project_name}/src/pyo2ipadist/assets/dist"):
        shutil.rmtree(f"{project_name}/src/pyo2ipadist/assets/dist")
    shutil.copytree("dist", f"{project_name}/src/pyo2ipadist/assets/dist")

    print("start edit the 'app.py' file")
    open(f"{project_name}/src/pyo2ipadist/app.py", "w+", encoding="utf-8").write(The_app_py_script)

    print("start creating/editing the 'localhost.py' file")
    open(f"{project_name}/src/pyo2ipadist/localhost.py", "w+", encoding="utf-8").write(The_localhost_py_script)

    print("Your app is being built and then opened on the iOS simulator..\nThis will take a few seconds..")
    process = subprocess.Popen(["cd pyo2ipadist\nbriefcase create iOS\nbriefcase build iOS\n"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    process.communicate()

    print("""

All work done!
Your app is in the `pyo2ipadist/build/pyo2ipadist/iOS/xcode`!
To run a simulator, use:
$ cd pyo2ipadist
$ briefcase run iOS

    """)