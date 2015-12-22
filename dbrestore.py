#!/usr/bin/python
###########################################################
#
# Orig Written by : Rahul Kumar
# Website: http://tecadmin.net
# Created date: Dec 03, 2013
# Last modified: Dec 03, 2013
# Tested with : Python 2.6.6
# Script Revision: 1.1
#
##########################################################

# Import required python libraries
import os
import time
import datetime

# MySQL database details to which backup to be done. Make sure below user having enough privileges to take databases backup. 
# To take multiple databases backup, create any file like /backup/dbnames.txt and put databses names one on each line and assignd to DB_NAME variable.

DB_HOST = 'localhost'
DB_USER = 'root'
DB_USER_PASSWORD = 'sanitized'
DB_NAME = '/Users/xalg/Google Drive/Current/Development/Python/db_backup/dblist.txt'
#DB_NAME = 'db_name'
BACKUP_PATH = '/Users/xalg/dbdumps/'

# Code for checking if you want to take single database backup or assinged multiple backups in DB_NAME.
print "checking for databases names file."
#database_list_command="mysql -u %s -p%s -h %s --silent -N -e 'show databases'" % (DB_USER,DB_USER_PASSWORD, DB_HOST)
if os.path.exists(DB_NAME):
    file1 = open(DB_NAME)
    multi = 1
    print "Databases file found..."
    print "Starting restore of all dbs listed in file " + DB_NAME
else:
    print "Databases file not found..."
    print "Starting restore of database " + DB_NAME
    multi = 0

if multi:
	in_file = open(DB_NAME,"r")
	flength = len(in_file.readlines())
	in_file.close()
	p = 1
	dbfile = open(DB_NAME,"r")

	while p <= flength:
	   db = dbfile.readline()   # reading database name from file
	   db = db[:-1]         # deletes extra line
	   createdb = "mysqladmin -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + "create " + db
	   restcmd = "mysql -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " < " + BACKUP_PATH + "/12092015-035345/" + db + ".sql"
	   #os.system(createdb)
	   os.system(restcmd)
	   p = p + 1
	dbfile.close()