import os
from config import *

for f in os.listdir(parsedDir):
    if(f != ".DS_Store"):
        base, ext = f.split('.')
        #prep = file('/Volumes/Data/Tecdoc-parsed/'+base+"."+ext, 'rb')
        myfile = open('/Volumes/Data/Tecdoc-parsed/'+base+"."+ext, 'rb')
        dest = file('/Volumes/Data/Tecdoc-combined/'+base+'.txt', 'a')
        for line in myfile:
            dest.write(line)
        
