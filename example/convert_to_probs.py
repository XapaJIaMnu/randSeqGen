#!/usr/bin/env python3
from sys import stdin, stdout
from math import exp

for line in stdin:
    line = line.strip().split()
    newline = []
    for item in line:
        try:
            num = float(item)
            newline.append(str(round(exp(num),4)))
        except ValueError:
            newline.append(item)
    stdout.write(" ".join(newline) + "\n")
