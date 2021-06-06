import time 
import os 
from colorama import Fore

RED = Fore.RED
RESET = Fore.RESET
BLUE = Fore.BLUE
DEBUG = True
""" 
all packages will be put here by name as to loop through and install them
if there are diffrent packages for both package manager then they will be written 
manualy or put into another list
"""
packages_usr = ["tmux", "vim", "sapd", "pulseaudio", "pulseaudio-bluetooth", "bashtop", "htop", "firefox", "code --classic", "gnome-tweaks", "unzip", "zip"]

# reboot command some for all systems 
def rebot():
    if DEBUG==True: print(f"{BLUE}not rebooting as debug is enabled{RESET}")
    else:
        if input(f"{RED}would you like to reboot this is reccomended [Y/n]{RESET}\n").lower().strip()=="n": os.system("sudo reboot now")

def warningdisk():
    num = len(packages_usr)
    print(f"{RED}//WARNING: this is going to install over {num} packages and repositorys are you sure you have enough room to continue? [y/n]{RESET}")
    if input("").lower().strip()=="n": exit()

class pacman:
    def __init__(self):
        warningdisk()
        self.update()
        self.manPBS()
        rebot()

    def update(self):
        os.system("sudo pacman -Syy sudo pacman -Syyy")

    def manPBS(self):
        for package in packages_usr:
            os.system(f"sudo pacman -Sy {package}")
        self.update()

class debian:
    def __init__(self):
        warningdisk()
        os.system("sudo apt upgrade")
        self.update()
        self.manPBS()
        rebot()

    def update(self):
        os.system("sudo apt update")

    def manPBS(self):
        for package in packages_usr:
            os.system("sudo apt-get install {package}")
        self.update()

def userPP():
    os.system("clear")
    user = input("pacman\ndebian\n\nplease pick a package manager: ")
    user = user.lower().strip()
    if user=="pacman": user = pacman()
    elif user=="debian": user = debian()
    else: userPP()

if __name__=="__main__":
    userPP()
