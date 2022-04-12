import shutil
import yaml
import os 
import pathlib
from datetime import datetime
from win32com.client import Dispatch

class command:
    def __init__(self,settingsfile,args = None):
        self.file = settingsfile
        self.args = args
        self.values = yaml.full_load(open(settingsfile))
        return

    def openinstance(self) -> None:
        term = self.args.open
        if term not in self.values["open"] :  raise ValueError("No shortcut saved for term")
        array = self.values["open"][term] 

        for item in array:
            os.startfile(item)

    def web(self) -> None :
        term = self.args.web
        if term  in self.values["web"] :  
            array = self.values["web"][term] 
        else: array = [term]

        for item in array:
            os.system(f"start {self.values['websettings']['browserkey']} {item}")
        return

    def createpyenv(self) -> None :
        # Folder name for python enviorment by default ; is data&time of folder creation
        foldername = datetime.now().strftime("%d%m%Y_%H%M%S")
        
        #opts dictionary to store parameters for creating python environment
        opts = {"dir":self.values['pyenv']['defaultdir'],"foldername":str(foldername),"file name":"program.py"}

        # Bypasses any prompts
        if self.args.yesall:
            opts = opts
        else:
            x = str(input("Do you want to create a standard python env with default params(y,n):"))
            if x == None: return
            if x in ['Y','y'] :
                opts = opts
            elif x in ['N','n']:
                a = str(input("Enter the folder to create environment (Enter !DEF to use default) : "))
                b = str(input("Enter name of folder to be created (Enter !DEF to use default): "))
                c = str(input("Enter name of python file (Enter !DEF to use default): "))
                if a != "!DEF" : opts["dir"] = a
                if b != "!DEF" : opts["foldername"] = b 
                if c != "!DEF" : opts["file name"] = c

        deffolder = pathlib.Path(opts["dir"])
        assert deffolder.is_dir(), "{} not found".format(str(deffolder))

        newdir = deffolder.joinpath(opts["foldername"])
        os.mkdir(newdir)

        string = "code -a {} -r".format(str(newdir))
        os.system(string)

        open(os.path.join(newdir,opts["file name"]),"x")


        store = self.values
        store['pyenv']['envdirs'].append(str(newdir))


        with open(self.file,'w') as file:
            documents = yaml.dump(store, file)

    def pydel(self) -> None :
        for i in self.values['pyenv']['envdirs']:
            try:shutil.rmtree(i)
            except:pass
        return

    def opensettings(self) -> None :
        os.startfile(self.file)
        return
    

    def version(self) -> str:
        parser = Dispatch("Scripting.FileSystemObject")
        version = parser.GetFileVersion('C:\\Program Files\\Prosid\\Do\\do.exe')
        return version
    
if __name__ == "__main__":
    x = command("sampledo.yaml",)


