#!/usr/bin/python

ON = '#'
OFF = '.'
X_SIZE = 100
Y_SIZE = 100


def count_active_neighbors(grid, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                    continue
            try:
                if grid[x+i][y+j] == ON:
                    if (x + i) >= 0 and (y + j) >= 0:
                        count += 1
            except IndexError:
                continue
    return count


def count_on(grid):
    return sum(line.count(ON) for line in grid)


def cell_next_state(on_or_off, num_neighbors):
    if on_or_off == ON and num_neighbors in [2, 3]:
        return ON
    elif on_or_off == OFF and num_neighbors == 3:
        return ON
    return OFF


def one_round(current_grid):
    temp_grid = [['' for _ in range(X_SIZE)] for _ in range(Y_SIZE)]
    for i in range(X_SIZE):
        for j in range(Y_SIZE):
            neighbor_count = count_active_neighbors(grid, i, j)

            if i in [0, X_SIZE-1] and j in [0, Y_SIZE-1]:
                next_state = ON
            else:
                next_state = cell_next_state(current_grid[i][j], neighbor_count)

            temp_grid[i][j] = next_state
    return temp_grid


def process_file(infile):
    initial_grid = list()
    for line in open(infile, 'r').readlines():
        initial_grid.append(list(line.strip()))

    initial_grid[0][0] = ON
    initial_grid[0][Y_SIZE-1] = ON
    initial_grid[X_SIZE-1][0] = ON
    initial_grid[X_SIZE-1][Y_SIZE-1] = ON
    return initial_grid


def print_grid_nicely(grid):
    for line in grid:
        print ''.join(line)

grid = process_file('day_18_input.txt')
for _ in range(100):
    grid = one_round(grid)  
    print count_on(grid)
