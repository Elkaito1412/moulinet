import os
import subprocess

try:
    parsedfile = open(".moulinet.conf")
except IOError:
    print '';
def	parseconfig(value):
	for line in parsedfile:
		if line.startswith(value):
			data = line.split("=");
	return((data[1].split(";"))[0])
