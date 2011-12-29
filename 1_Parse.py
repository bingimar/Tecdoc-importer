# -*- coding: utf-8 -*-
import os
from processing import Pool
import random
from config import *

d = os.path.dirname(destFile)
if not os.path.exists(d):
    os.mkdir(destFile)



def parse(params):
    base,ext = params
    if ext == 'dat':
        print "%s.%s" % (base, ext)
    if(os.path.isfile(configDir+base+'.txt')):
        print "Begin parsing: %s.%s" % (base, ext)
        configList = []
        for lines in open(configDir+base+'.txt', 'r'):
            line = lines.split(',')
            for l in line:
                configList.append(l)
        try:        
            dest = open(destFile+'/tecdoc_t'+base+'.'+ext, 'a')
        except IOError:
            print "Error: cant write the file %s.%s" % (base,ext)
        else:
            for line in open(extractedDir+"/"+base+"."+ext, "r"):

                if len(line) > 5:
                    begin = 0
                    end = 0
                    length = 0
                    output = ""
                    for i in configList:
                        length=int(i)
                        end = begin + length
                        output += line[begin:end]+";"
                        begin = end
                    dest.write(output+"\n")
            dest.close()
            print "Done parsing %s.%s" % (base, ext)
    else:
        print "File does not exist %s.%s" % (base, ext)

files = []
for f in os.listdir(extractedDir):
    if f != '.DS_Store':
        base, ext = f.split('.')
        if ext == 'dat' or int(ext):
            files.append((base,ext))

random.shuffle(files)
p = Pool()
p.map(parse, files)
