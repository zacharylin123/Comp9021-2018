# Randomly generates a binary search tree whose number of nodes
# is determined by user input, with labels ranging between 0 and 999,999,
# displays it, and outputs the maximum difference between consecutive leaves.
#
# Written by *** and Eric Martin for COMP9021

import sys
from random import seed, randrange
from binary_tree_adt import *

# Possibly define some functions
L3 = []
def travel(tree):
    if tree.value is None:
        return 
    if tree.left_node.value is None and tree.right_node.value is None:
        L3.append(tree.value)
    travel(tree.left_node)
    travel(tree.right_node)
def max_diff_in_consecutive_leaves(tree):

    travel(tree)
    gap = []
    if len(L3) > 1:
        for i in range(len(L3) - 1):
            gap.append(L3[i + 1] - L3[i])
    if L3 and len(L3) > 1:
        return max(gap)
    else:
        return 0
    
    # Replace pass above with your code


provided_input = input('Enter two integers, the second one being positive: ')
try:
    arg_for_seed, nb_of_nodes = provided_input.split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, nb_of_nodes = int(arg_for_seed), int(nb_of_nodes)
    if nb_of_nodes < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
tree = BinaryTree()
L1 = []
for _ in range(nb_of_nodes):
    datum = randrange(1000000)
    L1.append(datum)
    tree.insert_in_bst(datum)
print(L1)
print('Here is the tree that has been generated:')
tree.print_binary_tree()
print('The maximum difference between consecutive leaves is: ', end = '')
print(max_diff_in_consecutive_leaves(tree))
           
