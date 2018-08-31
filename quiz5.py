# Randomly fills a grid of size 10 x 10 with 0s and 1s and computes:
# - the size of the largest homogenous region starting from the top left corner,
#   so the largest region consisting of connected cells all filled with 1s or
#   all filled with 0s, depending on the value stored in the top left corner;
# - the size of the largest area with a checkers pattern.
#
# Written by *** and Eric Martin for COMP9021

import sys
from random import seed, randint
import copy

dim = 10
grid = [[None] * dim for _ in range(dim)]

def display_grid():
    for i in range(dim):
        print('   ', ' '.join(str(grid[i][j]) for j in range(dim)))

# Possibly define other functions

try:
    arg_for_seed, density = input('Enter two nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density = int(arg_for_seed), int(density)
    if arg_for_seed < 0 or density < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
# We fill the grid with randomly generated 0s and 1s,
# with for every cell, a probability of 1/(density + 1) to generate a 0.
for i in range(dim):
    for j in range(dim):
        grid[i][j] = int(randint(0, density) != 0)
print('Here is the grid that has been generated:')
display_grid()

size_of_largest_homogenous_region_from_top_left_corner  = 0
# Replace this comment with your code

def display_grid_new():
    for i in range(dim):
        print('   ', ' '.join(str(grid_new[i][j]) for j in range(dim)))
grid_new = copy.deepcopy(grid)


initial = grid[0][0]
def replace_by_star(i, j):
    global grid
    if grid[i][j] == initial:
        grid[i][j] = '*'
        if i:   # i != 0
            replace_by_star(i - 1, j)
        if i < dim - 1:
            replace_by_star(i + 1, j)
        if j:# j != 0
            replace_by_star(i, j - 1)
        if j < dim - 1:
            replace_by_star(i, j + 1)


replace_by_star(0, 0)

def count_1():
    count = 0
    for i in range(dim):
        for j in range(dim):
            if grid[i][j] == '*':
                count += 1
    return count

size_of_largest_homogenous_region_from_top_left_corner = count_1()




grid = copy.deepcopy(grid_new)




def change_by_star1(i, j): # down & right
    global grid
    if (j < dim - 1) and (grid[i][j] + grid[i][j + 1] == 1):
        grid_new[i][j] = '*'
        grid_new[i][j + 1] = '*'
        if j < dim - 1:
            change_by_star1(i, j + 1)
    if (i < dim -1 ) and (grid[i][j] + grid[i + 1][j] == 1):
        grid_new[i][j] = '*'
        grid_new[i + 1][j] = '*'
        if i < dim - 1:
            change_by_star1(i + 1, j)

def change_by_star2(i, j): # down & left
    global grid
    if (j > 0) and (grid[i][j] + grid[i][j - 1] == 1):
        grid_new[i][j] = '*'
        grid_new[i][j - 1] = '*'
        if j > 0:
            change_by_star2(i, j - 1)
    if (i < dim - 1) and (grid[i][j] + grid[i + 1][j] == 1):
        grid_new[i][j] = '*'
        grid_new[i + 1][j] = '*'
        if i < dim - 1:
            change_by_star2(i + 1, j)
def change_by_star3(i, j): # up & right
    global grid
    if (i > 0) and (grid[i][j] + grid[i - 1][j] == 1):
        grid_new[i][j] = '*'
        grid_new[i - 1][j] = '*'
        if i > 0:
            change_by_star3(i - 1, j)
    if (j < dim - 1) and (grid[i][j] + grid[i][j + 1] == 1):
        grid_new[i][j] = '*'
        grid_new[i][j + 1] = '*'
        if j < dim - 1:
            change_by_star3(i, j + 1)

def change_by_star4(i, j):  # up & left
    global grid
    if (j > 0) and (grid[i][j] + grid[i][j - 1] == 1):
        grid_new[i][j] = '*'
        grid_new[i][j - 1] = '*'
        if j > 0:
            change_by_star4(i, j - 1)
    if (i > 0) and (grid[i][j] + grid[i - 1][j] == 1):
        grid_new[i][j] = '*'
        grid_new[i - 1][j] = '*'
        if i > 0:
            change_by_star4(i - 1, j)


            
def count_2():
    count = 0
    for i in range(dim):
        for j in range(dim):
            if grid_new[i][j] == '*':
                count += 1
    return count
L = []

def call_f(i, j):
    grid_new[i][j] = '*'
    change_by_star1(i, j)
    change_by_star2(i, j)
    change_by_star3(i, j)
    change_by_star4(i, j)

for i in range(dim):
    for j in range(dim):
        grid_new = copy.deepcopy(grid)
        call_f(i, j)
        for a in range(dim):
            for b in range(dim):
                if grid_new[a][b] == '*':
                    call_f(a, b)
                    print(grid_new)
        L.append(count_2())




print('The size_of the largest homogenous region from the top left corner is '
      f'{size_of_largest_homogenous_region_from_top_left_corner}.'
     )

max_size_of_region_with_checkers_structure = max(L)
# Replace this comment with your code
print('The size of the largest area with a checkers structure is '
      f'{max_size_of_region_with_checkers_structure}.'
     )


