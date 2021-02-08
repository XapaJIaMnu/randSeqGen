#!/usr/bin/env python3
"""Generates a complete sequence of permutations"""
import sys
import itertools
from get_sec import get_uniq_chars_list

if __name__ == '__main__':
    num_chars = int(sys.argv[1])
    output_file = sys.argv[2]
    with open(output_file, 'w') as w:
        chr_arr = get_uniq_chars_list(num_chars)
        perms = [p for p in itertools.product(chr_arr, repeat=num_chars)]
        for line in perms:
            w.write(" ".join(line) + "\n")


