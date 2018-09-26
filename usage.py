from tcolors import *

def	usage():
	print tcolors.BOLD + """Usage :
""" + tcolors.OKGREEN + """init : """ + tcolors.ENDC + """initialise he moulinet in the folder.
""" + tcolors.BOLD + tcolors.OKGREEN + """purge : """ + tcolors.ENDC + """purge all moulinet files in current directory.
""" + tcolors.BOLD + tcolors.OKGREEN + """grademe : """ + tcolors.ENDC + """evaluate user files in the directory and write traces.
""" + tcolors.BOLD + tcolors.OKGREEN + """list :""" + tcolors.ENDC + """ list all supported projects. 
""" + tcolors.BOLD + tcolors.OKGREEN + """<exercise id> : """ + tcolors.ENDC + """use this directory as containing solution to exercise with the specified id.\n"""
