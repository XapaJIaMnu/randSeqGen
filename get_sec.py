#!/usr/bin/env python3
"""Generates a sequence of random characters"""
import argparse
import random

def parse() -> tuple[int, int, int, int, int, str]:
    """Argument parser"""
    parser = argparse.ArgumentParser(description="Generates a document with N lines of length from minlen to maxlen containing M uniq characters.")
    parser.add_argument('-n', '--num-lines', dest="N", required=True)
    parser.add_argument('-smin', '--sentence-length-min', dest="smin", required=True)
    parser.add_argument('-smax', '--sentence-length-max', dest="smax", required=True)
    parser.add_argument('-m', '--uniq-words', dest="M", required=True)
    parser.add_argument('-o', '--output-file', dest="O", required=True)
    parser.add_argument('-r', '--random-seed', dest="R", default="1")
    args = parser.parse_args()
    return (int(args.N), int(args.smin), int(args.smax), int(args.M), int(args.R), args.O)


def get_uniq_chars_list(num: int) -> list[str]:
    """Creates a list of uniq characters"""
    if num > 60:
        raise Exception("Only up to 60 uniq characters supported, you provided:", str(num))
    ret = []
    for i in range(65, 65 + num):
        ret.append(chr(i))
    return ret

def create_line(smin_: int, smax_: int, dictionary: list[str]) -> str:
    """Creates a line of between smin and smax random characters"""
    output_ = ""
    num_chars = random.randint(smin_, smax_)
    for i in range(num_chars):
        pos = random.randint(0, len(dictionary) - 1)
        char = dictionary[pos]
        output_ = output_ + char + " "
    output_ = output_[:-1] + "\n" # Remove trailing whitespace and add a newline character
    return output_



if __name__ == '__main__':
    num_lines, smin, smax, uniq_words, randseed, output = parse()
    random.seed(randseed)
    myvocab = get_uniq_chars_list(uniq_words)
    with open(output, "w") as out:
        for i in range(num_lines):
            out.write(create_line(smin, smax, myvocab))
