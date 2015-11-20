#!/usr/bin/env python

import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("fasta")
args = parser.parse_args()

with open(sys.argv[1], 'r') as gfp_fasta:
    for line in gfp_fasta:
        if line.startswith(">"):
            continue
        for fasta in line.strip():
            print ("Fasta File %d:" %  fasta)
