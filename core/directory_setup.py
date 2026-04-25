#Script that automatically find steam directory + tf2 directory
#I created it with help of chat gpt cuz I didn`t know how to do that`

import os
import sys
import json
import re
from json_util import Save_data

def getSteamPath():
     """Return default Steam installation paths for Windows/Mac/Linux."""
     if sys.platform.startswith("win"):
          possible =[
               os.path.expandvars(r"%PROGRAMFILES(x86)%\Steam"),
               os.path.expandvars(r"%PROGRAMFILES%\Steam"),
          ]
     elif sys.platform == "darwin": 
          possible =[os.path.expanduser("~/Library/Application Support/Steam")]
     else:
          possible =[os.path.expanduser("~/.local/share/Steam")]
     for p in possible:
          if os.path.exists(p):
               return p
     return None

def prase_libraryvdf(path):
     """Parse libraryfolders.vdf manually."""
     libraries = []

     with open(path,"r", encoding="utf-8") as f:
          text = f.read
      
    #/SteamLibrary matches
     matches = re.findall(r'"\d+"\s*"([^"]+)"', str(text))

     for m in matches:
          if os.path.isdir(m):
               libraries.append(os.path.join(m,"steamapps"))
     return libraries

def findTF2_json():
 steam_path = getSteamPath()
 if not steam_path:
          NO_steampath = {"found": False, "error": "Steam path not found"}
          Save_data(NO_steampath)

 liberary_file = os.path.join(steam_path, "steamapps","libraryfolders.vdf")
 if not os.path.exists(liberary_file):
      No_liberary_file = {"found": False, "error": "libraryfolders.vdf missing"}
      Save_data(No_liberary_file)
 libraries = prase_libraryvdf(liberary_file)

 #always include the main library from the steam path
 main_lib = os.path.join(steam_path, "steamapps")
 if os.path.isdir(main_lib):
      libraries.append(main_lib)

#TF2 MAINFEST
 mainfest_name = "appmanifest_440.acf" 
 for lib in libraries:
      mainfest_path = os.path.join(lib, mainfest_name)
      if os.path.exists(mainfest_path):
           #Install directory
         install_dir = os.path.join(lib, "common", "Team Fortress 2")
         tf2pathfound ={
                    "found": True,
                    "tf2_path": install_dir if os.path.isdir(install_dir) else None,
                    "manifest_path": mainfest_path,
                    "libraries": libraries,
                }
         Save_data(tf2pathfound)
      else:
           tf2pathnotfound =         {
            "found": False,
            "error": "TF2 manifest not found",
            "libraries_checked": libraries
        }
           Save_data(tf2pathnotfound) 

if __name__ == "__main__":
    findTF2_json()