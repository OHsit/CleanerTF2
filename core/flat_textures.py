from valve_parsers import VPKFile
from wand.image import Image
from wand.api import library

path_flat_tf2 = "cfg/flat.cfg"
path_flat_hl2 = "cfg/flat_hl2.cfg"

with open(path_flat_tf2, 'r') as fp:
    filepaths = fp.readlines()
    print(filepaths)
    textures_vpk = VPKFile("")

with open(path_flat_hl2, 'r') as fp:
    filepaths = fp.readlines()
    print(filepaths)
    textures_vpk_hl2 = VPKFile("")