#Script that automatically find steam directory + tf2 directory

import os
import sys
import json

TF2_SIGNATURES =[
 "tf.exe",
 os.path.join("tf","")
]
tf2_path = ""

def TF2DIR_Check(path):
 try:
    items = os.listdir(path)
 except PermissionError:
   return False
 except FileNotFoundError:
   return False
 
 for sig in TF2_SIGNATURES:
   if sig.endswith(os.sep):
     if sig[:-1] in items:
       return True
     else:
       if sig in items:
         return True
   return False
 
 def listDrives():
   drives = []
   if sys.platform.startswith("win"):
     for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
       d= f"{letter}:\\"
       if os.path.exists(d):
         drives.append(d)
       else:
         #linux support
         roots = ["/", "/mnt", "/media", "/Volumes"]
         for root in roots:
          if os.path.exists(root):
            drives.append(root)
     return drives
   

   def search_for_TF2():
     print("searching for TF2 directory...")
     drives = listDrives()

     matches = []
    
     for drive in drives:
      print(f"Scanning {drive} ...")
     for root, dirs, files in os.walk(drive, topdown=True):
       skip_dirs = ["Windows", "Program Files", "Program Files (x86)","$Recycle.Bin", "System32"]
       dirs[:] = [d for d in dirs if d not in skip_dirs]
     if TF2DIR_Check(root):
        print(f"FOUND TF2 DIRECTORY: {root}")
        matches.append(root)
     if not matches:
      print("\nNo TF2 directory found.")
     else:
       print("\nTF2 directories found:")
       for m in matches:
        print(" -", m)


     return matches 