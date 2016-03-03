#!/usr/bin/python
import re
from random import shuffle


def load_replacements_from_file(infile):
    replacements = []
    for line in open(infile, 'r').readlines():
        left = line.split()[0]
        right = line.split()[2]
        t = right, left
        replacements.append(t)

    return replacements


def string_to_capped_tokens(in_str):
    return re.findall('[A-Z][^A-Z]*', in_str)


def generate_replacement(formula, pair_tuple):
    formula.replace(pair_tuple[0], pair_tuple[1])


def keep_trying(formula, pairs):
    counter = 0
    while (1):
        if formula == 'e':
            break

        for r in pairs:
            if r[0] in formula:
                counter += 1
                formula = formula.replace(r[0], r[1], 1)
                print formula, counter


pairs = load_replacements_from_file('day_19_input_replacement_pairs.txt')
pairs = sorted(pairs, key=lambda a: len(a[0]))
pairs.reverse()

formula = open('day_19_input_chemical_string.txt', 'r').read()
keep_trying(formula, pairs)
