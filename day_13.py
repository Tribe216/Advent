#!/usr/bin/python
from collections import defaultdict
from itertools import permutations


def load_up_dict(infile):

    hap_ratings = defaultdict(dict)

    for line in open(infile, 'r').readlines():
        name = line.split()[0]
        gain_lose = line.split()[2]
        abs_rating = line.split()[3]
        partner = line.split()[-1][:-1]
        if gain_lose == 'gain':
            rating = int(abs_rating)
        else:
            rating = int(abs_rating) * -1

        hap_ratings[name][partner] = rating

    return hap_ratings


def get_results(hap_ratings):

    happy_total = -10000000000
    happy_combo = []

    for combo in permutations(hap_ratings.keys()):
        sub_total = 0
        for i, name in enumerate(combo):
            if name == 'Bart':
                continue
            if combo[i-1] == 'Bart':
                left = 0
            else:
                left = hap_ratings[name][combo[i-1]]
            if i == (len(combo) - 1):
                if combo[0] == 'Bart':
                    right = 0
                else:
                    right = hap_ratings[name][combo[0]]
            else:
                if combo[i+1] == 'Bart':
                    right = 0
                else:
                    right = hap_ratings[name][combo[i+1]]

            sub_total += left + right
        if sub_total > happy_total:
            happy_total = sub_total
            happy_combo = list(combo)
    return happy_total, happy_combo


hap_ratings = load_up_dict('./day_13_input.txt')

print get_results(hap_ratings)

# part 2
# add myself to dict with partner valu of zero for everyone
#

hap_ratings['Bart'] = {}

print get_results(hap_ratings)