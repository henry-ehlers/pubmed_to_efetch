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

# Funnction to replace whitespace and non-alphanumeric characters
def format_title_string(title_string):
	title_string = re.sub(r"[^\w\s]", '', title_string)
	title_string = "_".join(title_string.split())
	return title_string

# Define REGEX search patterns
pmid_pattern  = re.compile(r"^PMID- (\d+)$")
title_pattern = re.compile(r"^TI  - ([\s\S]+)$")
rolling_title = re.compile(r"^      ([\s\S]+)$")

# Open output file
esearch_file  = open(args['out'], 'w+')

# Initialize Entry ID and Title + rolling title
entry_pmid    = None
entry_title   = None
part_title    = None
title_ongoing = False

# Load File Contents Line-By-Line
with open(args['in']) as pubmed_file:

	# Iterate over each line
	for line in pubmed_file:
		
		# Find PMID
		if pmid_pattern.match(line):

			# Save PMID and move to next line
			entry_pmid  = pmid_pattern.search(line).group(1)
			continue

		# Find title
		if title_pattern.match(line):

			# Extract and Format Title for Esearch
			entry_title = title_pattern.search(line).group(1)
			entry_title = format_title_string(entry_title)

			# Indicate title may be ongoing and move to next line
			title_ongoing = True
			continue
		
		# Extract Rolling title to next line
		if rolling_title.match(line) and title_ongoing:

			# Extract and Format Ongoing Title for Esearch
			part_title = rolling_title.search(line).group(1)
			part_title = format_title_string(part_title)

			# Append part title to complete title and move to next line
			entry_title = entry_title + "_" + part_title
			continue

		# End search for multi-line title
		if (not rolling_title.match(line)) and title_ongoing:

			# Reset ongoing title and move to next iteration
			title_ongoing = False
			continue
			
		# Save Entry
		if entry_pmid and entry_title and not title_ongoing:

			# save to file
			esearch_file.write("{}\t{}\n".format(entry_pmid, entry_title))

			# reset title and pmid
			entry_pmid  = None
			entry_title = None
			part_title  = None

# Close all file connections
esearch_file.close()
pubmed_file.close()