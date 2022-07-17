from cx_Freeze import setup, Executable
import os
import shutil
import yaml

build_exe_options = {'packages':['pathlib','argparse','yaml','os','datetime','win32com','sys'], #pacakges used
                     'excludes':['tkinter'],'includes':['commands'], 
                     "include_msvcr": True,
                     'include_files':['icon.ico','doo.bat'],
                     "build_exe" : "C:\\Program Files\\Prosid\\Do"}

path = "C:\\ProgramData\\Prosid\\Do"


if os.path.isdir("C:\\Program Files\\Prosid\\Do"):shutil.rmtree("C:\\Program Files\\Prosid\\Do")

if os.path.isfile(os.path.join(path,"dosettings.yaml")):
    sample = open('sampledo.yaml')
    sampledata = yaml.full_load(sample)

    existing = open(os.path.join(path,"dosettings.yaml"))
    existingdata = yaml.full_load(existing)

    for i,j in sampledata.items():
        existingdata[i] = j | existingdata[i] 

    with open(os.path.join(path,"dosettings.yaml"),'w') as file:
        documents = yaml.dump(existingdata, file)

else:
    os.makedirs(path,exist_ok=True)
    newfile = open(os.path.join(path,"dosettings.yaml"),'x')
    sampledata = yaml.full_load(open('sampledo.yaml'))
    with open(os.path.join(path,"dosettings.yaml"),'w') as file:
        documents = yaml.dump(sampledata, file)

base = None
executables = [Executable(
            "cli.py",
            target_name = "do",
            copyright="Copyright (C) 2022 Prosid",
            base=base,
            icon="icon.ico",
            shortcutName="do",
            shortcutDir="do",)]

setup(
    name="do",
    version="1.0",
    author = "Sidharth S",
    description="Customizable macro tasker",
    executables=executables,
    options={
        "build_exe": build_exe_options,
    },
)

print("Installation complete !")