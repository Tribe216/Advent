#!/usr/bin/python
from collections import defaultdict, Counter
from itertools import combinations_with_replacement


def check_dict_subset(big_dict, small_dict):
    return all((k in big_dict and big_dict[k] == v) for k, v in small_dict.iteritems())


def check_dict_subset_special(big_dict, small_dict):
    for k, v in small_dict.iteritems():
        if k in ['cats:', 'trees:']:
            if k in big_dict and big_dict[k] > v:
                return False
        elif k in ['pomeranians:', 'goldfish:']:
            if k in big_dict and big_dict[k] < v:
                return False
        else:
            if k in big_dict and big_dict[k] != v:
                return False
    return True


def load_up_clues_dict(infile):

    clues = defaultdict(dict)

    for line in open(infile, 'r').readlines():
        clues[line.split()[0]] = int(line.split()[1])

    return dict(clues)


def load_up_stats_dict(infile):

    aunt_stats = defaultdict(dict)

    for line in open(infile, 'r').readlines():
        aunt_num = int(line.split()[1][:-1])
        stat_1_name = line.split()[2]
        stat_1_val = int(line.split()[3][:-1])
        stat_2_name = line.split()[4]
        stat_2_val = int(line.split()[5][:-1])
        stat_3_name = line.split()[6]
        stat_3_val = int(line.split()[7])
        aunt_stats[aunt_num] = {
            stat_1_name: stat_1_val,
            stat_2_name: stat_2_val,
            stat_3_name: stat_3_val,
        }

    return dict(aunt_stats)


aunt_stats = load_up_stats_dict('day_16_input_aunt_stats.txt')
clues_dict = load_up_clues_dict('day_16_input_clues.txt')

for aunt_num, stats in aunt_stats.iteritems():
    if check_dict_subset_special(clues_dict, stats):
        print aunt_num
