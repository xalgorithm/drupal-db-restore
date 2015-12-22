#!/usr/bin/env python
# -*- coding: utf-8 -*-

#find settings.php in Drupal
import os
import re
import pymysql as mdb
import sys
HOST = "localhost"
USER = "root"

FILESVAR = []
settingsfile = 'settings.php'
OUTPUTPATH = "/Users/xalg/settings_file.txt"
MYPASSLINE = re.compile("^\s*('password' =>)")
SITENAME = re.compile("^\s*('database' =>)")
NEWPATTERN = re.compile("(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{1,20}")

with open("/Users/xalg/filenames.txt", "w") as a:
	for path, subdirs, files in os.walk(r'/var/sites'):
	    for filename in files:
	        if filename == settingsfile:
			f = os.path.join(path, filename)
			a.write(str(f) + os.linesep)

def makethechange() :
	in_file = open("/Users/xalg/filenames.txt","r")
	flength = len(in_file.readlines())
	p = 1
	while p <= flength:
	   myfname = in_file.readline()   # reading database name from file
	   grek(myfname,SITENAME)
	   grok(myfname,MYPASSLINE)
	   changepass(MYPASSLINE,SITENAME)
		   p = p + 1
	in_file.close()

def grok (conffile,passline) :
    try:
        for i, line in enumerate(open(conffile)):
            for match in re.finditer(passline, line):
                thismatch = line.strip()
                myline = re.findall(NEWPATTERN,thismatch)
                return myline[0].strip('\'')

    except IOError as e:
        print "Unable to find the file you're looking for"
    except RuntimeError:
        print "Error in your syntax"
    except:
        print "Unexpected error:", sys.exec_info()[0]
def grek (conffile,dbline) :
    try:
        for i, line in enumerate(open(dbline)):
            for match in re.finditer(passline, line):
                thismatch = line.strip()
                myline = re.findall(SITENAME,thismatch)
                return myline[0].strip('\'')

    except IOError as e:
        print "Unable to find the file you're looking for"
    except RuntimeError:
        print "Error in your syntax"
    except:
        print "Unexpected error:", sys.exec_info()[0]

def changepass (password,dbname) :
    con = mdb.connect(host='localhost',
                          user='root',
                          password='sanitized',
                          db=dbname,
                          cursorclass = mdb.cursors.DictCursor)
	try:
        with con.cursor() as cur:
            sql = 'CREATE DATABASE IF NOT EXISTS' + dbname
            cur.execute(sql)
        con.commit()
        with con.cursor() as cur:
            sql = "'CREATE USER 'xalg'@'127.0.0.1' IDENTIFIED BY 'sanitized';'"
            cur.execute(sql)
        except mdb as e:
            print "Unable to find the file you're looking for"
        except RuntimeError:
            print "Error in your syntax"
        except:
            print "Unexpected error:", sys.exec_info()[0]
    #grant ALL ON *.* TO 'xalg'@'localhost';