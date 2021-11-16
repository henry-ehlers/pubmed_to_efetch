import argparse
import sys
import os
import re

# Read Input File from command line
parser=argparse.ArgumentParser()
parser._optionals.title = "Flag Arguments"
parser.add_argument('-in',
	help    = "Input file to parse. Must be of type 'PUBMED'.", 
	default = '%#$')
parser.add_argument('-out',
	help    = "Output file to which to parse output. Default = 'output.txt'",
	default = "output.txt")
args = vars(parser.parse_args())

# Ensure input file was specified 
if args['in']=='%#$' or not os.path.isfile(args['in']):
    print ("Error: Must specify valid input PUBMED file.")
    exit(1)

# Load File Contents Line-By-Line
with open(args['in']) as pubmed_file:
	for line in pubmed_file:
		print(line)
