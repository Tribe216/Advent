#!/usr/bin/python

houses_dict = {}
moves = {
    'v': [0, -1],
    '<': [-1, 0],
    '^': [0, 1],
    '>': [1, 0]
}

num_santas = 2

cp = [[0, 0] for x in range(num_santas)]

move_input = open('day_3_input.txt', 'r').read()

for char_index in range(len(move_input)):
    cur_santa = char_index % num_santas
    houses_dict[str(cp[cur_santa])] = True
    cp[cur_santa] = [x + y for x, y in zip(cp[cur_santa], moves[move_input[char_index]])]
    print len(houses_dict)
