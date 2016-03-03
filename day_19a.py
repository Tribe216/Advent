#!/usr/bin/python
from collections import defaultdict
import re


def load_replacements_from_file(infile):
    replacements = defaultdict(list)
    for line in open(infile, 'r').readlines():
        left = line.split()[0]
        right = line.split()[2]
        replacements[left].append(right)

    return dict(replacements)


def string_to_capped_tokens(in_str):
    return re.findall('[A-Z][^A-Z]*', in_str)


def generate_replacement(tokens, pairs):
    for e, t in enumerate(tokens):
        if t not in pairs:
            continue
        for r in pairs[t]:
            new_token_seq = tokens[:]
            new_token_seq[e] = r
            new_string = ''.join(new_token_seq)
            yield new_string

pairs = load_replacements_from_file('day_19_input_replacement_pairs.txt')
formula = open('day_19_input_chemical_string.txt', 'r').read()
tokenized_formula = string_to_capped_tokens(formula)
distinct_formulas = set()
for i, x in enumerate(generate_replacement(tokenized_formula, pairs)):
    distinct_formulas.add(x)

print len(distinct_formulas)
