import os, shutil, subprocess, zipfile, random
from processing import Pool
from zipfile import ZipFile
from config import *


def unzip(params):
    base, ext = params
    zf = zipfile.ZipFile(rawDir+'/'+base+'.'+ext, 'r')
    for name in zf.namelist():
        if name != 'PIC/':
            print name
            zf.extract(name, extractDir)

files = []
for f in os.listdir(rawDir):
    if(f.endswith('exe')):
        base, ext = f.split('.')
        if(len(base) == 3):
            files.append((base,ext))
p=Pool()
p.map(unzip, files)
        
