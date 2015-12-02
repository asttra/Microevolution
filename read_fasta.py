#!/usr/bin/env python

import sys
import random
import argparse

#mutation functions
def mutate_base(base):
    if base == 'A':
        new_base = random.choice('CGT')
    elif base == 'C':
        new base = random.choice('AGT')
    elif base == 'G':
        new_base == random.choice('ACT')
    else:
        new_base == random.choice('ACG')
    return new_base

def mutate(seq):
    base_list = list(seq)
    position_to_mutate = random.randint(0, len(base_list)-1)
    old_base = base_list[position_to_mutate]
    new_base = mutate_base(old_base)
    base_list[position_to_mutate] = new_base
    new_sequence = "".join(base_list)
    return new_seq


parser = argparse.ArgumentParser()
parser.add_argument("bases")
args = parser.parse_args()

with open(args.bases, 'r') as gfp_fasta:
    for line in gfp_fasta:
        if line.startswith(">"):
            continue
        print line.strip()
        mutated_sequence = mutate(bases)
        print mutated_sequence
