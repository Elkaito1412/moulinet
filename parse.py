import os
import subprocess

parsedfile = open(".moulinet.conf")

def	parseconfig(value):
	for line in parsedfile:
		if line.startswith(value):
			data = line.split("=");
	return((data[1].split(";"))[0])
