# PubMed Reference List to PMF

## The Data 

A simple command-line executable script designed to convert PubMed reference list to PMF, in order to enable batch downloading of the listed publications via *efetch*. The PubMed reference file is a list of metadata fields and those fields' values separated by whitespace and a dash. Each metadata field and value pair is separated from the next by a newline, though some fields (such as the title in the example below) can fill mulitple lines:

{
	PMID- 32302568
	OWN - NLM
	STAT- MEDLINE
	DCOM- 20201123
	LR  - 20210623
	IS  - 1097-4172 (Electronic)
	IS  - 0092-8674 (Print)
	IS  - 0092-8674 (Linking)
	VI  - 181
	IP  - 2
	DP  - 2020 Apr 16
	TI  - The Human Tumor Atlas Network: Charting Tumor Transitions across Space and Time at 
	      Single-Cell Resolution.
	PG  - 236-249
	LID - S0092-8674(20)30346-9 [pii]
	LID - 10.1016/j.cell.2020.03.053 [doi]
}

The only two fields of interest for *efetch* however are the PMID field (a unique identifier within the PubMed library), and (optionally) its title. This data is extracted and saved in a PMF file, which consists of pairs of tab-separated PMID's and titles. Each such pair is separated from the next by a newline character:

{
	32302568	The_Human_Tumor_Atlas_Network_Charting_Tumor_Transitions_across_Space_and_Time_at_SingleCell_Resolution_SingleCell_Resolution
	25504833	Viewing_the_proteome_how_to_visualize_proteomics_data
}

## Input Arguments

This script is to be called from the command line, and allows for two input arguments:

```bash
{
	python3 pubmed_to_efetch.py -in ./foo -out ./bar
}
```

*-in* defines the directory to the input PubMed reference file, where as *-out* defines the directory of the output PMF file. 