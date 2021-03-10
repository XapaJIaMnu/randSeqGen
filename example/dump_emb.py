#!/usr/bin/env python3
import sys
import numpy as np
from collections import defaultdict
from itertools import combinations, permutations
from intervaltree.intervaltree import IntervalTree


def get_barycentric_region(perm):

    assert len(perm) <= max(perm) + 1
    basis = np.eye(max(perm) + 1)

    points = []

    for i in range(1, len(perm) + 1):
        indices = perm[:i]
        points.append(basis[indices, :].mean(axis=0))
    return np.array(points)


def get_prob_range(perms):
    ranges = defaultdict(IntervalTree)
    for perm in perms:
        barycentric_region_hull = get_barycentric_region(perm)
        mins = barycentric_region_hull.min(axis=0)
        maxs = barycentric_region_hull.max(axis=0)
        for i in range(len(perm)):
            if mins[i] != maxs[i]:
                ranges[i].addi(mins[i], maxs[i])
    for r in ranges.values():
        r.merge_overlaps()
    return ranges


def braid_arrangement(ww):
    vecs = []
    for i in range(len(ww)):
        for j in range(i + 1, len(ww)):
            vecs.append(ww[i] - ww[j])
    return np.array(vecs)


def detect_regions(ww):
    RADIUS = 2
    NUM_SAMPLES = 720 * 2
    valid_regions = set()
    xx = np.pi * 2 * np.arange(NUM_SAMPLES) / NUM_SAMPLES
    xx = np.vstack([np.cos(xx), np.sin(xx)])
    sign_vectors = (ww.dot(xx) > 0.).astype(int)
    valid_regions.update(tuple(row) for row in sign_vectors.T)
    return valid_regions


def decode_inversion_bit_string(s):

    idx = 0
    perm_length = int(np.sqrt(len(s) * 2) + 1)
    perm = np.arange(perm_length)

    # We effectively undo the permutation specified by
    # the inversion set on the increasing order
    for i in range(perm_length):
        for j in range(i + 1, perm_length):
            if s[idx]:
                perm[i] += 1
                perm[j] -= 1
            idx += 1

    # invert the inverted sort
    perm = np.argsort(perm)
    return perm


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " path/to/model/dir")
        exit(1)
    a = np.load(sys.argv[1] + "/model.npz")
    W = a['decoder_Wemb']
    print('Softmax weights', W)

    vocab = dict()
    print("\nOrdering correspondence:")
    with open(sys.argv[1] + "/vocab.rand.yml", 'r') as file:
        for line in file:
            line = line.strip()
            w, idx = line.split(': ')
            vocab[int(idx)] = w
            print(line)

    ww = braid_arrangement(W)
    regions = detect_regions(ww)
    counter = defaultdict(int)
    perms = set()
    for region in regions:
        # print(region)
        pp = decode_inversion_bit_string(region)
        perms.add(tuple(pp))
        counter[pp[-1]] += 1
        # print(''.join(map(str, pp)))
        assert(len(set(pp)) == len(W))
    # print(len(regions))
    # print(counter)

    # print(perms)
    # perms = tuple(permutations(np.arange(7)))
    #
    print('')
    prob_ranges = get_prob_range(perms)
    for k, v in prob_ranges.items():
        print('Class %s probability bounds: ' % vocab[k], v)

    print('')
    position_counters = [set() for i in range(len(W))]
    for perm in perms:
        for i, p in enumerate(perm):
            position_counters[i].add(vocab[p])

    for i, occ in enumerate(position_counters):
        print('Classes that can be in position %d' % i, occ)

    # CONDITION_MAX_CLASS = 1
    # print('\nCondition on the argmax being %d\n' % CONDITION_MAX_CLASS)
    # truncated_perms = [p[1:] for p in perms if p[0] == CONDITION_MAX_CLASS]
    #
    # for p in [pp for pp in perms if pp[0] == CONDITION_MAX_CLASS]:
    #     print(p)
    # print('')
    #
    # for p in truncated_perms:
    #     print(p)
    #
    # prob_ranges = get_prob_range(truncated_perms)
    # for k, v in prob_ranges.items():
    #     print('Class %d probability bounds: ' % k, v)
    #
    # position_counters = [set() for i in range(len(W) - 1)]
    # for perm in truncated_perms:
    #     for i, p in enumerate(perm):
    #         position_counters[i].add(p)
    #
    # for i, occ in enumerate(position_counters):
    #     print('Classes that can be in position %d' % i, occ)
    #
    # # plt.scatter(*W.T)
    # # for i in range(len(W)):
    # #     plt.text(W[i][0], W[i][1], str(i))
    # # plt.show()
