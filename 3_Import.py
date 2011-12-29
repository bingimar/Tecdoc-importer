import MySQLdb
import os, sys, subprocess, traceback, time
from processing import Pool
from config import *

conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='')
cursor = conn.cursor()

def getCol(table):
    cursor.execute("SHOW COLUMNS FROM %s;" % table)
    columns = cursor.fetchall()
    c = []
    for cc in columns:
        if cc[0] != 'id':
            c.append(cc[0])
    return c

def myimport():
    for f in os.listdir(parsedFiles):
        if f != '.DS_Store':
            base, ext = f.split('.')
            base = str(base)
            if base.startswith('tecdoc_t'):
                table = base
                if table not in ['tecdoc_t201', 'tecdoc_202']:
                    colString = ','.join(getCol(table))
                    if(ext == 'txt'):
                        subprocess.Popen("mysqlimport --delete --local -u root --password= --fields-terminated-by=\';\' --lines-terminated-by=\'\\n\' database_name \'/Volumes/Data/Tecdoc-combined/"+base+"."+ext+"\'", shell=True)


myimport()
