# Randomly fills a grid of size 10 x 10 with 0s and 1s,
# in an estimated proportion of 1/2 for each,
# and computes the longest leftmost path that starts
# from the top left corner -- a path consisting of
# horizontally or vertically adjacent 1s --,
# visiting every point on the path once only.
#
# Written by Eric Martin for COMP9021


import sys
from random import seed, randint

from queue_adt import *


dim = 10
grid = [[0] * dim for i in range(dim)]

def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' ', grid[i][j], end = '')
        print()
    print()
def new(position,a):
    if a == 'N':
        return (position[0] - 1,position[1])
    if a == 'S':
        return (position[0] + 1,position[1])
    if a == 'E':
        return (position[0], position[1] + 1)
    if a == 'W':
        return (position[0], position[1] - 1)
def leftmost_longest_path_from_top_left_corner():
    directions = {'N': (-1, 0),'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}
    next_directions = {'N': ('W', 'N', 'E'), 'S': ('E', 'S', 'W'), 'E': ('N', 'E', 'S'), 'W': ('S', 'W', 'N')}
    if grid[0][0] == 0:
        return []
    paths = Queue()
    path_direction = Queue()
    path_direction.enqueue('E')
    paths.enqueue([(0, 0)])
    result = []
    while not paths.is_empty():
        output = paths.dequeue()
        print(output)
        if len(output) > len(result):
            result = output
 #       print(result)
        direction1 = path_direction.dequeue()
        current_position = output[-1]
        if len(output) > 1:
            print('len')
            previous_position = output[-2]
 #           print(previous_position)
            if output[-1][0] - output[-2][0] == 1 and output[-1][1] - output[-2][1] == 0:
                d = 'E'
            elif output[-1][0] - output[-2][0] == -1 and output[-1][1] - output[-2][1] == 0:
                d = 'W'
            elif output[-1][0] - output[-2][0] == 0 and output[-1][1] - output[-2][1] == 1:
                d = 'N'
            elif output[-1][0] - output[-2][0] == 0 and output[-1][1] - output[-2][1] == -1:
                print('s')
                d = 'S'
        else:
            print('e')
            d = 'E'
        for e in next_directions[d]:
 #           new_position = (current_position[0] + directions[e][0], current_position[1] + directions[e][1])
            new_position = new(current_position, e)
            if new_position[0] < 0 or new_position[0] >9 or new_position[1] < 0 or new_position[1] > 9:
                continue
            if new_position in output:
                continue
            if grid[new_position[0]][new_position[1]] == 0:
                continue
            path_enqueue = list(output)
            path_enqueue.append(new_position) 
            paths.enqueue(path_enqueue) 
            path_direction.enqueue(e)
    return result


provided_input = input('Enter one integer: ')
try:
    seed_arg = int(provided_input)
except:
    print('Incorrect input, giving up.')
    sys.exit()

seed(seed_arg)
# We fill the grid with randomly generated 0s and 1s,
# with for every cell, a probability of 1/2 to generate a 0.
for i in range(dim):
    for j in range(dim):
        grid[i][j] = randint(0, 1)
print('Here is the grid that has been generated:')
display_grid()

path = leftmost_longest_path_from_top_left_corner()
if not path:
    print('There is no path from the top left corner')
else:
    print('The leftmost longest path from the top left corner is {}'.format(path))
