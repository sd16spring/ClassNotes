"""
Test timing execution with the timeit module

Examples are from the Day 17 exercises in analyzing algorithmic performance
"""

import timeit
from random import randint

# Code to be tested

def generate_random_dna(n):
    """ Generate a random DNA sequence of length n """
    dna_list = []
    nucleotides = ['A','C','G','T']
    for i in range(n):
        r = randint(0,3)
        dna_list.append(nucleotides[r])
    return "".join(dna_list)

def get_complement(c):
    """ Returns the complimentary nucleotide to c """
    if c == 'A':
        return 'T'
    if c == 'C':
        return 'G'
    if c == 'G':
        return 'C'
    if c == 'T':
        return 'A'

def reverse_complement_1(dna):
    """ Method 2 for computing the reverse complementary sequence of DNA
        for the specfied DNA sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    >>> reverse_complement_1("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> reverse_complement_1("CCGCGTTCA")
    'TGAACGCGG'
    """
    return_val = ""
    for c in dna:
        return_val = get_complement(c) + return_val 
    return return_val

def reverse_complement_2(dna):
    """ Method 1 for Computing the reverse complementary sequence of DNA
        for the specfied DNA sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    >>> reverse_complement_2("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> reverse_complement_2("CCGCGTTCA")
    'TGAACGCGG'
    """
    return_val = []
    for c in reversed(dna):
        return_val.append(get_complement(c))
    return "".join(return_val)


# Run if called from the command line
if __name__ == "__main__":

	# Setup code (if any) to call before test
	setup = "from __main__ import generate_random_dna, reverse_complement_1, reverse_complement_2 ; dna = generate_random_dna(2000)"
	ntrials = 1000

	# Run tests for 1000 executions each
	print "RC1 time:", timeit.timeit("reverse_complement_1(dna)", setup=setup, number=ntrials)
	print "RC2 time:", timeit.timeit("reverse_complement_2(dna)", setup=setup, number=ntrials)
