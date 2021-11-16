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

# Define REGEX search patterns
pmid_pattern  = re.compile(r"^PMID- (\d+)$")
title_pattern = re.compile(r"^TI  - ([\s\S]+)$")

# Load File Contents Line-By-Line
with open(args['in']) as pubmed_file:

	for line in pubmed_file:
		
		if pmid_pattern.match(line):

			# Save PMID
			entry_pmid  = pmid_pattern.search(line).group(1)

		if title_pattern.match(line):

			# Save Title
			entry_title = title_pattern.search(line).group(1)

			# Remove all non-alphanumeric characters from title
			entry_title = re.sub(r"[^\w\s]", '', entry_title)

			# Replace all whitespace between alphanumreci with '_'
			entry_title = "_".join(entry_title.split())
			print(entry_title)