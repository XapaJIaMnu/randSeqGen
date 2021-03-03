#!/usr/bin/env python3
import sys
import numpy as np
if len(sys.argv) != 2:
    print("Usage: " + sys.argv[0] + " path/to/model/dir")
    exit(1)
a = np.load(sys.argv[1] + "/model.npz")
print(a['decoder_Wemb'])

print("Ordering correspondence:")
with open(sys.argv[1] + "/vocab.rand.yml", 'r') as file:
    for line in file:
        print(line.strip())
