import os
import sys

#from modules import playerctl
# from modules import os
from modules import network
from modules import ram
from modules import gpu
from modules import cpu

def Pyfetch():
    if(sys.platform == "linux"):
        print("Do you want to install all dependencies? ")
        if(input() == "y"):
            os.system("nix-shell -p python313Packages.python")
        else:
            print("Exiting...")

Pyfetch()