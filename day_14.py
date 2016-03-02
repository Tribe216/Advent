#!/usr/bin/python
from collections import defaultdict
from itertools import permutations


def load_up_dict(infile):

    reindeer_stats = defaultdict(dict)

    for line in open(infile, 'r').readlines():
        name = line.split()[0]
        flt_speed = int(line.split()[3])
        flt_time = int(line.split()[6])
        rest_time = int(line.split()[-2])
        reindeer_stats[name] = {
            "flt_speed": flt_speed,
            "flt_time": flt_time,
            "rest_time": rest_time}

    return dict(reindeer_stats)


def distance_traveled(dsl, t):
    fly_and_rest_cycle_time = (dsl['flt_time'] + dsl['rest_time'])
    whole_cycles = t / fly_and_rest_cycle_time
    total_fly_time = whole_cycles * dsl['flt_time']
    remain_time = t % fly_and_rest_cycle_time
    if remain_time >= dsl['flt_time']:
        total_fly_time += dsl['flt_time']
    else:
        total_fly_time += remain_time
    return (total_fly_time * dsl['flt_speed'])

reindeer_stats_dict = load_up_dict('./day_14_input.txt')

leaderboard = defaultdict()

for i in range(1, 2504):
    print '------'
    dist_array = defaultdict(list)

    for deer, deer_stats in reindeer_stats_dict.iteritems():
        dist_array[distance_traveled(deer_stats, i)].append(deer)

    leading_distance = max([d for d in dist_array])
    for deer_leader in dist_array[leading_distance]:
        if deer_leader in leaderboard:
            leaderboard[deer_leader] += 1
        else:
            leaderboard[deer_leader] = 1

    for i, j in leaderboard.iteritems():
        print i, j