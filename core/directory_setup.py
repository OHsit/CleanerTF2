#Script that automatically find steam directory + tf2 directory
#I created it with help of chat gpt cuz I didn`t know how to do that`

import os
import sys
import json
import re

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
     matches = re.findall(r'"\d+"\s*"([^"]+)"', text)

     for m in matches:
          if os.path.isdir(m):
               libraries.append(os.path.join(m,"steamapps"))
     return libraries

def findTF2_json():
     steam_path = getSteamPath()
     if not steam_path:
          return json.dumps({"found": False, "error": "Steam path not found"}, indent=4)