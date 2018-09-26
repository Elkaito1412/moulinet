#this ia a try at making a mini local version of the moulinette
import os
from os import walk
import sys
import subprocess
from tcolors import *
from usage import *
from parse import parseconfig

bindir = os.path.realpath(__file__)
version = "01"

try:
	configfile = open(".moulinet.conf", "r")
except IOError:
	print(tcolors.WARNING + "WARNNG : directory not initialised" + tcolors.ENDC)
print tcolors.HEADER + "-----Moulinet v" + version + "-----\n" + tcolors.ENDC
if len(sys.argv) != 2 :
	usage();
	exit();
elif sys.argv[1] == "init":
	print "initialising moulinet in folder : " + tcolors.OKBLUE + os.path.abspath(__file__) + '\n'
	os.system("cp ~/.moulinet/moulinet.default.conf ./.moulinet.conf")
elif sys.argv[1] == "purge":
	print "purging all moulinet files in folder : " + tcolors.OKBLUE + os.path.abspath(__file__) + '\n'
	os.system("rm -f .moulinet.conf")
elif sys.argv[1] == "list":
	filenum = 0;
	for (dirpath, dirnames, filenames) in walk("./projects"):
    		for i in filenames:
			print ' ' + tcolors.OKBLUE + str(filenum) + ' : ' + tcolors.ENDC + i
			filenum = filenum + 1
		print '\n'
    		break
elif sys.argv[1] == "grademe":
	try:
		configfile
	except NameError:
		print( tcolors.BOLD + tcolors.FAIL + "please initialise directory and chose project before grading !\n")
		exit()
	if "proj_id = null" in configfile.read():
		print(tcolors.BOLD + tcolors.FAIL + "project not chosen \n")
	else:
		plugins = []
        	for (dirpath, dirnames, filenames) in walk("./projects"):
                	plugins.extend(filenames);
		print(tcolors.BOLD + tcolors.OKGREEN + " Grading on project : " + plugins[int(parseconfig("proj_id"))] + tcolors.ENDC)
else:
	plugins = []
	for (dirpath, dirnames, filenames) in walk("./projects"):
		plugins.extend(filenames);
	try:
		projectid = int(sys.argv[1])
	except ValueError as verr:
		print " error in user input\n"
		exit()
	except Exception as ex:
		print " error in user input\n"
		exit()
	if(projectid) < len(filenames):
		print(" loading project : " + filenames[projectid])
		os.system("sed -i 's/proj_id=[0-9]\+;/proj_id=" + str(projectid) + ";/g' .moulinet.conf")
	else:
		print(" project not available at the moment\n")
