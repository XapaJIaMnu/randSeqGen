#!/usr/bin/env python3
"""Computes normalises the embeddings according to https://www.aclweb.org/anthology/N18-1031.pdf"""

import sys
import math
import numpy as np

if __name__ == '__main__':
    inmodel = np.load(sys.argv[1])
    emb_mat = inmodel['decoder_Wemb']
    maxnorm = None
    for i in range(len(emb_mat)):
        norm = np.linalg.norm(emb_mat[i])
        if maxnorm is None:
            maxnorm = norm
        else:
            maxnorm = max(maxnorm, norm)
    print(emb_mat)
    maxnorm = math.ceil(maxnorm)
    for i in range(len(emb_mat)):
        norm = np.linalg.norm(emb_mat[i])
        for j in range(len(emb_mat[i])):
            emb_mat[i][j] = (maxnorm*emb_mat[i][j])/norm

    print(emb_mat)
    out_model = dict(inmodel)
    out_model['decoder_Wemb'] = emb_mat
    np.savez(sys.argv[2], **out_model)
