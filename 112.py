import os
import shutil

source = "C:/source"
des = "C:/dest"

listOfFile = os.listdir(source)

for file in listOfFile:
    root,exe = os.path.splitext(file)
    dirTree={
        "Images": [".png",".jpg"],
        "Models": [".obj",".fbx",".zip"]
    }
    path1 = source+'/'+file
    path2 = des+'/'+"Document files"
    path3 = des + '/' + "Document files" + '/' + file

    if exe in [".png",".jpg"]:
        shutil.move(path1,path2)
    if exe in [".obj",".fbx",".zip"]:
        shutil.move(path1, path2)

    if os.path.exists(path2):
        print("move"+file)
        shutil.move(path1,path3)
    else:
        os.makedirs(path2)
        print("move" + file)
        shutil.move(path1, path3)