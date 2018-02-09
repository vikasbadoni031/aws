#!/usr/bin/python

import boto3
import subprocess
import json
import time
import psycopg2
import os



location_to_be_scanned="/home/vikas/quant/"

#os.chdir("/home/vikas/quant/Insert_one_time" )
#for filename in os.listdir("/home/vikas/quant/Insert_one_time"):
def one_time_insert(filename):
    with open(filename, 'r') as f:
        data = f.read()
#.replace("\r\n", '')
    #print data
    try:
        con = psycopg2.connect(dbname='databasename', host='hostname',port='5439', user='username', password='pwd')
        cur = con.cursor()
        cur.execute("BEGIN")
        cur.execute(data)
        cur.execute("COMMIT")
    except Exception as e:
        print "Insert failed for tablename=" + filename +  "reason" + str(e)



for root, dirs, files in os.walk(location_to_be_scanned):
    for f in files:
        fullpath = os.path.join(root, f)
        if os.path.split(fullpath)[1] == 'full_insert_redshift.sql':
            print fullpath
            one_time_insert(fullpath)
