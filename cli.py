import argparse
from commands import command
import sys

class docli:
    def __init__(self) -> None:
        
        parser = argparse.ArgumentParser(description='All in one macro tasker')

        parser.add_argument('--createpyenv','-py', 
                            action = "store_true",
                            dest   = "pyenv",
                            help   = "Interactive python environment creator")
        
        parser.add_argument('--list','-ls', 
                            action = "store_true",
                            dest   = "list",
                            help   = "List all saved settings")
        
        parser.add_argument('-y','-yesall', 
                            action = "store_true",
                            dest   = "yesall",
                            help   = "Send yes to any prompts, run command on default settings")

        parser.add_argument('--version', 
                            action = "store_true",
                            dest   = "version",
                            help   = "View version of running application")

        parser.add_argument('--uninstall', 
                            action = "store_true",
                            dest   = "unins",
                            help   = "Uninstall the application.")

        parser.add_argument('--open','-o', 
                            action  = "store",
                            dest    = "open", 
                            metavar = "brave",
                            help    = "Run command with prescribed shortcut",)
                            
        parser.add_argument('--settings','-s', 
                            action = "store_true",
                            dest   = "settings",
                            help   = "Open settings of program / modify shortcuts")          

        parser.add_argument('--deletepy','-dp', 
                            action = "store_true",
                            dest   = "pydel",
                            help   = "Delete any created python environment directories")  

        parser.add_argument('--web','-w',
                            action  = "store",
                            dest    = "web",   
                            metavar = "youtube",
                            help    = "Open websites from predefined shortcuts",)

        args = parser.parse_args()


        # Namespace(pyenv=False, list=False, open=None, settings=False, web=None)
        cmd = command('C:\\ProgramData\\Prosid\\Do\\dosettings.yaml',args=args)

        if args.open : cmd.openinstance()

        if args.pydel : cmd.pydel()

        if args.pyenv : cmd.createpyenv()

        if args.settings : cmd.opensettings()

        if args.web : cmd.web()

        if args.list :
            for i in cmd.values :
                print(f"{i} =>")
                print(cmd.values[i])
                print("")
            
        if args.version : print(cmd.version())

        if args.unins : 
            x = str(input("Do you want to uninstall the application and its associated files (Y/N) : "))
            if x not in ['Y','y'] : return
            cmd.uninstall()
        pass


if __name__ == "__main__":
    x = docli()
    sys.exit()