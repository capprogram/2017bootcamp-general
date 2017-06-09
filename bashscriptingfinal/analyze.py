#!/usr/bin/env python
# Takes an input file as first command line argument, 
# reads the first two columns then prints the first and a transformation of the second to an output file,
# where the name of the output file is given as the second command line argument

import sys, math

try:
  inputFile = sys.argv[1]
  outputFile = sys.argv[2]
except:
  print "Usage:", sys.argv[0],"<input file> <output file>"
  sys.exit(1)


ifile = open(inputFile, 'r')
ofile = open(outputFile, 'w')

def transFunc(y):
  if y>=0.5:
    return math.pow(y,2)*math.exp(-y)
  else:
    return 0.0

ofile.write("X\tY**2\n")

for line in ifile:
  data = line.split()
  x = float(data[0])
  fy = math.pow( float( data[1] ), 2 )
  ofile.write("%g\t%.5e\n" % (x,fy) )

ifile.close()
ofile.close()
