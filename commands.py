import yaml
import os 
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


    def opensettings(self) -> None :
        os.startfile(self.file)
        return
    

    def version(self) -> str:
        parser = Dispatch("Scripting.FileSystemObject")
        version = parser.GetFileVersion('C:\\Program Files\\Prosid\\Do\\do.exe')
        return version
    
if __name__ == "__main__":
    x = command("sampledo.yaml",)


