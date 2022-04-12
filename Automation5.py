import shutil,os

def selectiveCopy(folder,extensions,destFolder):
    folder=os.path.abspath(folder)
    print(folder)
    destFolder=os.path.abspath(destFolder)
    print(destFolder)
    print('Looking in '+ folder+ ' for files with extensions of ', ','.join(extensions))
    for foldername,subfolders,filenames in os.walk(folder):
        print("***",foldername, "**", subfolders , "*",filenames)
        for file in filenames:
            name, extension = os.path.splitext(file)

            if extension in extensions:
                fileAbsPath = foldername + os.path.sep + file
                print('Coping', fileAbsPath, 'to', destFolder)
                shutil.copy(fileAbsPath, destFolder)
    


print("Current Working Directory " , os.getcwd())
os.chdir("C:\\Users\\name")
extensions=['.py','.txt']
folder='Documents\\LeetCode'
destFolder='Desktop'
selectiveCopy(folder, extensions, destFolder)