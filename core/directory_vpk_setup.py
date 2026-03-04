import json
import os
import sys

with open('cfg/directories_debug.json', 'r') as file:
    data = json.load(file)
    tf2_path = data["tf2_path"]
    #debug resons 
    print(tf2_path)