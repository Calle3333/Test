import os
import sys
from time import sleep
from shutil import copyfile
from pathlib import Path

os.chdir(str(Path.home()))
os.chdir(os.path.join(os.getcwd(),"Desktop\p5Scripts"))


#if in p5Scripts
#path=os.getcwd()

pathOrg=os.path.join(os.getcwd(),"ScriptsFiles")
pathOrg=os.path.join(pathOrg,"p5.js sketch prefab")
pathOrgE=os.path.join(pathOrg,"libraries")

if not os.path.exists(pathOrg):
    print("Error: Missing files")
    print(pathOrg)
    print(os.getcwd())
    sleep(5)
    sys.exit()

projectName = input("Name: ")

os.makedirs(projectName)
os.chdir(projectName)



copyfile(os.path.join(pathOrg,"index.html"),"index.html")
copyfile(os.path.join(pathOrg,"sketch.js"),"sketch.js")

os.makedirs("libraries")
os.chdir("libraries")

copyfile(os.path.join(pathOrgE,"p5.dom.js"),"p5.dom.js")
copyfile(os.path.join(pathOrgE,"p5.js"),"p5.js")
copyfile(os.path.join(pathOrgE,"p5.sound.js"),"p5.sound.js")
