#this ia a try at making a mini local version of the moulinette
import os
import sys
from tcolors import *
from usage import *

print tcolors.HEADER + "-----Moulinet v01-----\n" + tcolors.ENDC
if len(sys.argv) != 2 :
	usage();
	exit();
