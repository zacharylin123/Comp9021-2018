# Written by **** for COMP9021

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):
        node = self.head
        count = -1
        small_val = self.head.value
        while node.next_node:
            if node.next_node.value < small_val:
                small_val = node.next_node.value
            node = node.next_node
        if self.head.value == small_val:
        
            a = self.head
            node2 = a
            while node2.next_node.next_node:
                node2 = node2.next_node
            node.next_node = a
            self.head = node
            node2.next_node = None
        elif self.head.next_node.value == small_val:
            pass 
        else:
            a = self.head
            
            node3 = self.head
            while node3.next_node.next_node.value != small_val:
                node3 = node3.next_node
            node.next_node = a
            self.head = node3.next_node
            node3.next_node = None
        a1 = self.head
        even_node = self.head
        odd_node = self.head.next_node
        begin_odd = odd_node
        begin_even = even_node
        while True:
            if even_node.next_node and even_node.next_node.next_node:
                even_node.next_node = even_node.next_node.next_node
                even_node = even_node.next_node
            else:
                break
            if odd_node.next_node and odd_node.next_node.next_node:
                odd_node.next_node = odd_node.next_node.next_node
                odd_node = odd_node.next_node
            else:
                break
        odd_node.next_node = begin_even
        even_node.next_node = None
        self.head = begin_odd
        while begin_odd.next_node:
            begin_odd = begin_odd.next_node
        begin_odd.next = begin_even
        times = 0
        node = self.head
        while node:
            times += 1
            node = node.next_node

        times1 = (times // 2 - 1)
        while self.head.next_node != a1:
            even_node = self.head
            odd_node = self.head.next_node
            begin_odd = odd_node
            while True:
                if even_node.next_node and even_node.next_node.next_node:
                    even_node.next_node = even_node.next_node.next_node
                    even_node = even_node.next_node
                else:
                    break
                if odd_node.next_node and odd_node.next_node.next_node:
                    odd_node.next_node = odd_node.next_node.next_node
                    odd_node = odd_node.next_node
                else:
                    break
            even_node.next_node = begin_odd
            odd_node.next_node = None
       

           












        
##        node4 = self.head.next_node
##        while True:
##            if node4.next_node:
##                a = node4.next_node.next_node
##                node4.next_node.next_node.next_node = node4.next_node
##                node4.next_node.next_node = None
##                node4.next_node = node4
##                node4 = a
##                print(node4.value)
##                print(node4.next_node.value)
##                node4 = node4.next_node
##                print(node4.value)
##            else:
##                break
##

       
##        node4 = self.head
##        self.head = node4.next_node           
##        while True:
##            if node4.next_node.next_node:
##                print('1')
##                a = node4.next_node.next_node.next_node
##                b = node4
##                node4.next_node.next_node.next_node.next_node = node4.next_node.next_node
##                node4.next_node.next_node.next_node = None  # how to deal with the last one
##                node4.next_node.next_node = b
##                node4.next_node = a
##                print(node4.value)
##                node4 = node4.next_node
##                print(f'node4.value{node4.value}')
##                print(node4.next_node.value)
##                #print(node4.next_node.next_node.value)
##           # elif node4.next_node == None:
##                #break
##            else:
##                break
##                node4.next_node.next_node = node4
##                node.next_node = None
##                break
##           
##
##
##        
##
