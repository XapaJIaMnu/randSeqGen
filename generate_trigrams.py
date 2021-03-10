#!/usr/bin/env python3
"""Generates a sequence of random characters"""
import argparse
import random

def parse():
    """Argument parser"""
    parser = argparse.ArgumentParser(description="Generates a document with N lines of length from minlen to maxlen containing M uniq characters.")
    parser.add_argument('-slen', '--sentence-length', dest="slen", type=int, required=True)
    parser.add_argument('-m', '--uniq-words', dest="uniq_words", type=int, required=True)
    parser.add_argument('-o', '--output-file', dest="output_file", required=True)
    parser.add_argument('-r', '--random-seed', dest="random_seed", default="1")
    args = parser.parse_args()
    return args


def get_uniq_chars_list(num: int) -> list:
    """Creates a list of uniq characters"""
    if num > 60:
        raise Exception("Only up to 60 uniq characters supported, you provided:", str(num))
    ret = []
    for i in range(65, 65 + num):
        ret.append(chr(i))
    return ret


if __name__ == '__main__':
    args = parse()
    vocab = get_uniq_chars_list(args.uniq_words)

    prefix = vocab[0]
    REPEATS = 3

    # for line_num in range(args.num_lines):
    lines = []
    line = [prefix] * (args.slen - 1)
    for i in range(1, len(vocab)):
        # Earlier letters have higher frequency
        for j in range(len(vocab) - i):
            for n in range(REPEATS):
                l = ' '.join(line + [vocab[i]]) + '\n'
                lines.append(l)
    # random.shuffle(lines)

    with open(args.output_file, "w") as out:
        out.writelines(lines)
