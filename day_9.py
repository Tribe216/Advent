#!/usr/bin/python
from itertools import permutations

from collections import defaultdict

distances = []
locations = set()
for line in open('day_9_input.txt','r').readlines():
    src, dst, distance = line.rstrip().replace(' to ',' ').replace(' = ', ' ').split(' ')
    distances.append([src, dst, distance])
    locations.add(src)
    locations.add(dst)

def get_distance(city1,city2):
    for a in distances:
        if city1 in a and city2 in a:
            return int(a[2])

best_path_so_far = [[],0]

combo_list = list(permutations(locations))
combo_list = combo_list[:len(combo_list)/2]
for cur_path_list in combo_list:
    path_length = 0
    for i in range(len(cur_path_list)-1):
        path_length += get_distance(cur_path_list[i],cur_path_list[i + 1]) 

    # print path_length, cur_path_list
    if path_length > best_path_so_far[1]:
        best_path_so_far[0] = cur_path_list
        best_path_so_far[1] = path_length

print best_path_so_far