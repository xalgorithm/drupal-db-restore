import ConfigParser
import os
import time


config = ConfigParser.ConfigParser()
config.read("db_conn.cnf")
username = config.get('client', 'user')
password = config.get('client', 'password')
hostname = config.get('client', 'host')

filestamp = time.strftime('%Y-%m-%d')

# Get a list of databases with :
database_list_command="mysql -u %s -p%s -h %s --silent -N -e 'show databases'" % (username, password, hostname)
for database in os.popen(database_list_command).readlines():
    database = database.strip()
    if database == 'performance_schema':
        continue
    if database == 'information_schema':
        continue

    filename = "/Users/xalg/dbdumps/%s-%s.sql" % (database, filestamp)
    os.popen("mysqldump -u %s -p%s -h %s -e --opt -c %s | gzip -c > %s.gz" % (username, password, hostname, database, filename))