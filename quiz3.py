from random import seed, randint
import sys
from collections import defaultdict
import math

def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))
'''
def triangles_in_grid():
    return {}
    # Replace return {} above with your code
'''
# Possibly define other functions

try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()




def generate_grid():
    for i in range(dim):
        for j in range(dim):
            if grid[i][j] != 0:
                grid[i][j] = 1
generate_grid()
def finalgrid(i, j):    #1 create triangle list
    count = 1
    flag = True
    size = 1
    if grid[i][j] != 0:
        for x in range(i + 1, dim):
            while flag:
                if (j - size >= 0) and (j + size <dim) and (x <= dim):
                    if 0 in grid[x][(j - size): (j + size + 1)]:
                        flag = False
                        break
                    else:
                        count += 1
                        size += 1
                        grid[i][j] = count
                        break
                        if x == dim:
                            flag = False
                            break
                else:
                    flag = False
                    break



def generate_to_count():    #2 also generte triangle
    for i in range(0, dim):
        for j in range(0, dim):
            finalgrid(i, j)
generate_to_count()


dict1 = {}


def dictN():#__________________________________
    listtuple = []
    limit = math.ceil((dim - 1) / 2)
    control = 1
    if limit == 1:
        control = 2
    for d in range(2, limit + control):
        sum1 = sum((row.count(d) for row in grid))
        if sum1 != 0:
            t1 = (str(d), sum1)
            listtuple.append(t1)
    listtuple = (sorted(listtuple, key = lambda x: x[1]))
    dict1['N'] = listtuple
    if dict1['N']:
        pass
    else:
        del dict1['N']
    return dict1
dictN()


generate_grid()
def generate_to_W(L):
    rotated = list(zip(*L[::-1]))
    L = [list(e) for e in rotated]
    return L

grid = generate_to_W(grid)

generate_to_count()





def dictW():    #__________________________________
    listtuple = []
    control = 1
    limit = math.ceil((dim - 1) / 2)
    if limit == 1:
        control = 2
    for d in range(2, limit + control):
        sum1 = sum((row.count(d) for row in grid))
        if sum1 != 0:
            t1 = (str(d), sum1)
            listtuple.append(t1)
    listtuple = (sorted(listtuple, key = lambda x: x[1]))
    dict1['W'] = listtuple
    if dict1['W']:
        pass
    else:
        del dict1['W']
    return dict1
dictW()



generate_grid()
def generate_to_E(L):
    rotated = list(zip(*L[::-1]))
    rotated2 = list(zip(*rotated[::-1]))
    L = [list(e) for e in rotated2]
    return L

grid = generate_to_E(grid)

generate_to_count()
def dictE():    #__________________________________
    listtuple = []
    control = 1
    limit = math.ceil((dim - 1) / 2)
    if limit == 1:
        control = 2
    for d in range(2, limit + control):
        sum1 = sum((row.count(d) for row in grid))
        if sum1 != 0:
            t1 = (str(d), sum1)
            listtuple.append(t1)
    listtuple = (sorted(listtuple, key = lambda x: x[1]))
    dict1['E'] = listtuple
    if dict1['E']:
        pass
    else:
        del dict1['E']
    return dict1
dictE()


def generate_to_S(L):
    rotated = list(zip(*L[::-1]))
    rotated2 = list(zip(*rotated[::-1]))
    rotated3 = list(zip(*rotated2[::-1]))
    L = [list(e) for e in rotated3]
    return L

generate_grid()
grid = generate_to_S(grid)
generate_to_count()

def dictS():    #__________________________________
    listtuple = []
    control = 1
    limit = math.ceil((dim - 1) / 2)
    if limit == 1:
        control = 2
    for d in range(2, limit + control):
        sum1 = sum((row.count(d) for row in grid))
        if sum1 != 0:
            t1 = (str(d), sum1)
            listtuple.append(t1)
    listtuple = (sorted(listtuple, key = lambda x: x[1]))
    dict1['S'] = listtuple
    if dict1['S']:  # if dict["S"] = None then delete dict["S"]
        pass
    else:
        del dict1['S']
    return dict1
dictS()

def triangles_in_grid():
    return dict1
    



# A dictionary whose keys are amongst 'N', 'E', 'S' and 'W',
# and whose values are pairs of the form (size, number_of_triangles_of_that_size),
# ordered from largest to smallest size.
triangles = triangles_in_grid()
for direction in sorted(triangles, key = lambda x: 'NESW'.index(x)):
    print(f'\nFor triangles pointing {direction}, we have:')
    for size, nb_of_triangles in triangles[direction]:
        triangle_or_triangles = 'triangle' if nb_of_triangles == 1 else 'triangles'
        print(f'     {nb_of_triangles} {triangle_or_triangles} of size {size}')

