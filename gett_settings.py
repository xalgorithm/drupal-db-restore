#!/usr/bin/env python
#find settings.php in Drupal
import fnmatch
import os

MYDIR = "/var/sites"
FILENAME = "settings.php"
OUTPUTPATH = "/Users/xalg/settings_file.txt"
PASSFILE = "/Users/xalg/passfile.txt"
resname = []

#find all of the settings.php files in the given dir
def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                resname = os.path.join(root, basename)
                yield resname


	for resname in find_files('/var/sites', 'settings.php'):
		print "Found " + resname
		f = open(OUTPUTPATH,'w')
		f.write(resname + "\n") # python will convert \n to os.linesep
		f.close()

#find the password in the settings file
#
#def find_settings(OUTPUTPATH):
#	if os.path.exists(OUTPUTPATH):
#		for line in open(OUTPUTPATH).readlines():
#	    	settings = line.strip()
#		    f = open(PASSFILE,'w')
#			f.write(settings + "\n") # python will convert \n to os.linesep
#			f.close()
def main():
	find_files(MYDIR, FILENAME)


if __name__ == "__main__":
    main()