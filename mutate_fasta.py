#!/usr/bin/env python

import sys
import random
import argparse

def mutate_base(base):
    if base == 'A':
        new_base = random.choice('CGT')
    elif base == 'C':
        new_base = random.choice('AGT')
    elif base == 'G':
        new_base = random.choice('ACT')
    else:
        new_base = random.choice('ACG')
    return new_base

def mutate(seq):
    base_list = list(seq) # turn string to list b/c strings are immutable
    position_to_mutate = random.randint(0, len(base_list)-1)
    old_base = base_list[position_to_mutate]
    new_base = mutate_base(old_base)
    base_list[position_to_mutate] = new_base
    new_seq = "".join(base_list)
    return new_seq

def main():
    # Parse command line args
    parser = argparse.ArgumentParser()
    parser.add_argument('--fasta', '-f', required=True)
    args = parser.parse_args()

    # Open fasta file and read it line by line
    with open(args.fasta) as fastafile:
        for line in fastafile:
            if line.startswith(">"):
                sys.stdout.write(line)
            else:
                sequence = line.strip()
                mutated_sequence = mutate(sequence)
                print(mutated_sequence)


##########################

if __name__ == '__main__':
    main()
