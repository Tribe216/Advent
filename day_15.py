#!/usr/bin/python
from collections import defaultdict, Counter
from itertools import combinations_with_replacement


def ingredient_combo_generator(stats_dict):
    ingredient_names = list(stats_dict.keys())
    print ingredient_names

    for i in combinations_with_replacement(ingredient_names, 100):
        yield dict(Counter(i))


def get_score_of_combo(ingredient_stats, combo_dict):
    score = 1
    total_cals = 0
    relevant_props = ['c', 'd', 'f', 't']
    for prop in relevant_props:
        prop_score = 0
        for ing_name, count in combo_dict.iteritems():
            prop_score += count * ingredient_stats[ing_name][prop]
        score *= max(0, prop_score)

        total_cals = 0
        for ing_name, count in combo_dict.iteritems():
            total_cals += count * ingredient_stats[ing_name]['x']

    return {'score': score, 'combo': str(combo_dict), 'cals': total_cals}


def load_up_dict(infile):

    ingredient_stats = defaultdict(dict)

    for line in open(infile, 'r').readlines():
        ingredient = line.split()[0].lower()[:-1]
        capacity = int(line.split()[2][:-1])
        durability = int(line.split()[4][:-1])
        flavor = int(line.split()[6][:-1])
        texture = int(line.split()[8][:-1])
        calories = int(line.split()[10])
        ingredient_stats[ingredient] = {
            "c": capacity,
            "d": durability,
            "f": flavor,
            "t": texture,
            "x": calories
        }

    return dict(ingredient_stats)

stats = load_up_dict('day_15_input.txt.bak')

top_score = {'score': 0}
for c in ingredient_combo_generator(stats):
    sc = get_score_of_combo(stats, c)
    if sc['score'] > top_score['score']:
        top_score = sc

print top_score
