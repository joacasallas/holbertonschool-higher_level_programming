#!/usr/bin/python3
"""Write a class Node that defines a node of a singly linked list"""


class Node():
    """defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value
    
    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if next_node != None or if next_node != Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList():
    """defines a singly linked list"""
    def __init__(self):
        self.__head = 0
    
    def sorted_insert(self, value):
        for 

        



    
