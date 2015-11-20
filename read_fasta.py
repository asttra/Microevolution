#!/usr/bin/env python

import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("fasta")
args = parser.parse_args()

with open(sys.argv[1], 'r') as fasta:
    for line in fasta:
        if line.startswith(">"):
            continue
        for fasta in line.strip():
            print ("Fastfa File %d:" %  fasta)
