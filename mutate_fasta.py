#!/usr/bin/env python

import sys
import random

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
    # Open fasta file and read it line by line
    with open(sys.argv[1]) as fastafile:
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
