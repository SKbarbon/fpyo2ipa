import os
import zipfile
import shutil

def Unzip_asset ():
    asset_path = str(__file__).replace("Tools/unzip_assets.py", "assets/pyo2ipadist.zip")
    if not os.path.isfile(asset_path):
        raise FileNotFoundError("Cannot found the assets.")
    
    if os.path.isdir("pyo2ipadist"):
        shutil.rmtree("pyo2ipadist")

    with zipfile.ZipFile(asset_path, "r") as zip_ref:
        zip_ref.extractall("pyo2ipadist")
    
    shutil.copytree("pyo2ipadist/pyo2ipadist", "_pyo2ipadist")
    shutil.rmtree("pyo2ipadist")
    shutil.move("_pyo2ipadist", "pyo2ipadist")

    #? Edit the pyproject.toml file.
    AppName = input("Write the name of your app: ")
    Describe = input("Write a small descibe of your app:")
    if str(AppName).replace(" ", "") == "": AppName = "fpyo2ipa"
    if '"' in str(AppName): AppName = "fpyo2ipa"
    if '"' in str(Describe): Describe = "fpyo2ipa"
    print("write your appname and describe..")
    read_file = open("pyo2ipadist/pyproject.toml", encoding="utf-8").read()
    read_file = str(read_file).replace("_here_the_app_name_", AppName)
    read_file = str(read_file).replace("_here_the_describe_of_app_", Describe)

    open("pyo2ipadist/pyproject.toml", "w+", encoding="utf-8").write(read_file)