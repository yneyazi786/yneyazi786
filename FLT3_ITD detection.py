import argparse
import math
from functools import reduce
from sys import argv

def sum_list(lst):
    return sum(lst)

def max_list(lst):
    return max(lst)

def min_list(lst):
    return min(lst)

def dumper(obj):
    import pprint
    pprint.pprint(obj)

def ceil_value(val):
    return math.ceil(val)

def floor_value(val):
    return math.floor(val)

def main():
    parser = argparse.ArgumentParser(description="Your script description")
    # Add your script options here
    parser.add_argument('--option', help='Option help')
    args = parser.parse_args()
    print(args.option)
    
if __name__ == "__main__":
    main()
"""
NAME
    FLT3_ITD_ext - Process BAM files or FASTQ files for FLT3-ITDs
"""

import argparse

def process_files(input_file):
    # Function to process BAM or FASTQ files for FLT3-ITDs
    # Add your file processing logic here
    pass

def main():
    parser = argparse.ArgumentParser(description="Process BAM or FASTQ files for FLT3-ITDs")
    parser.add_argument('input_file', help='The BAM or FASTQ file to process')
    args = parser.parse_args()

    process_files(args.input_file)

if __name__ == "__main__":
    main()

"""
NAME
    FLT3_ITD_ext - Process BAM files or FASTQ files for FLT3-ITDs

SYNOPSIS
    --bam, -b    Input BAM file (either this or fastq1+2 required)
    --typeb, -t  Reads to extract from input BAM (defaults to "targeted" [FLT3-aligned]; or can be "loose" or "all")
    --fastq1, -f1    Input FASTQ1 (either fastq1+2 or BAM required)
    --fastq2, -f2    Input FASTQ2 (either fastq1+2 or BAM required)
    --output, -o     Output path (required)
    --ngstype, -n    NGS platform type (defaults to "HC" [hybrid capture]; or can be "amplicon", "NEB", or "Archer")
    --genome, -g     Genome build (defaults to "hg19"; or can be "hg38")
    --adapter, -a    Trim adapters (defaults to true; assumes Illumina)
    --web, -w        Create HTML webpages for each ITD call (defaults to false)
    --umitag, -u     BAM tag holding UMIs in the input BAM file for fgbio (defaults to ""; standard is "RX")
    --strat, -s      Strategy for UMI assignment used in fgbio GroupReadsByUmi (defaults to "adjacency")
    --probes, -p     Probes/baits file basename (defaults to ""); assumes FASTA file, BWA index files
    --minreads, -mr  Minimum number of supporting reads to be included in VCF (UMI-based if umitag set)
    --debug, -d      Save all intermediate files (defaults to false)
    --help, -h       Print this help

VERSION
    1.1
"""

import argparse

def process_files(bam, typeb, fastq1, fastq2, output, ngstype, genome, adapter, web, umitag, strat, probes, minreads, debug):
    # Add your file processing logic here
    pass

def main():
    parser = argparse.ArgumentParser(description="Process BAM or FASTQ files for FLT3-ITDs")
    parser.add_argument('--bam', '-b', help='Input BAM file (either this or fastq1+2 required)')
    parser.add_argument('--typeb', '-t', help='Reads to extract from input BAM (defaults to "targeted" [FLT3-aligned]; or can be "loose" or "all")')
    parser.add_argument('--fastq1', '-f1', help='Input FASTQ1 (either fastq1+2 or BAM required)')
    parser.add_argument('--fastq2', '-f2', help='Input FASTQ2 (either fastq1+2 or BAM required)')
    parser.add_argument('--output', '-o', required=True, help='Output path (required)')
    parser.add_argument('--ngstype', '-n', default='HC', help='NGS platform type (defaults to "HC" [hybrid capture]; or can be "amplicon", "NEB", or "Archer")')
    parser.add_argument('--genome', '-g', default='hg19', help='Genome build (defaults to "hg19"; or can be "hg38")')
    parser.add_argument('--adapter', '-a', action='store_true', help='Trim adapters (defaults to true; assumes Illumina)')
    parser.add_argument('--web', '-w', action='store_true', help='Create HTML webpages for each ITD call (defaults to false)')
    parser.add_argument('--umitag', '-u', default='', help='BAM tag holding UMIs in the input BAM file for fgbio (defaults to ""; standard is "RX")')
    parser.add_argument('--strat', '-s', default='adjacency', help='Strategy for UMI assignment used in fgbio GroupReadsByUmi (defaults to "adjacency")')
    parser.add_argument('--probes', '-p', default='', help='Probes/baits file basename (defaults to ""); assumes FASTA file, BWA index files')
    parser.add_argument('--minreads', '-mr', type=int, help='Minimum number of supporting reads to be included in VCF (UMI-based if umitag set)')
    parser.add_argument('--debug', '-d', action='store_true', help='Save all intermediate files (defaults to false)')
    args = parser.parse_args()

    process_files(args.bam, args.typeb, args.fastq1, args.fastq2, args.output, args.ngstype, args.genome, args.adapter, args.web, args.umitag, args.strat, args.probes, args.minreads, args.debug)

if __name__ == "__main__":
    main()
