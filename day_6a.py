#!/usr/bin/python

light_grid = [[0 for x in range(1000)] for y in range(1000)]


def count_on():
    count = 0
    for x in range(1000):
        for y in range(1000):
            count += light_grid[x][y]

    return count


def modify_range(start, end, command):
    for x in range(start[0], end[0]+1):
        for y in range(start[1], end[1]+1):
            if command == 'on':
                light_grid[x][y] += 1
            elif command == 'off':
                light_grid[x][y] = max(light_grid[x][y] - 1, 0)
            elif command == 'toggle':
                light_grid[x][y] += 2


def process_line(in_line):
    in_line = in_line.rstrip().replace(' through ', ',').replace(' ', ',')
    # print in_line
    spl = in_line.split(',')
    # print spl

    command = spl[-5]
    start_pos = [int(spl[-4]), int(spl[-3])]
    end_pos = [int(spl[-2]), int(spl[-1])]

    modify_range(start_pos, end_pos, command)


in_file = open('day_6_input.txt', 'r')

for line in in_file.readlines():
    process_line(line)

print count_on()



