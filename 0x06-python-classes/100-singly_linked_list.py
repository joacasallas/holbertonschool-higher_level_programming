#!/usr/bin/python3
"""Write a class Node that defines a node of a singly linked list"""


class Node():
    """defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """Initialization object
        Arguments: 
        data: linked list
        next_node: node to insert
        """
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
        if value != None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

    def __str__(self):
        return str(self.__data)

class SinglyLinkedList():
    """defines a singly linked list"""
    def __init__(self):
        """Initialization object"""        
        self.__head = None
    
    def sorted_insert(self, value):
        new = Node(value)
        tmp = self.__head
        if tmp is None or tmp.data >= value:
            if tmp:
                new.next_node = tmp
            self.__head = new
            return
        while tmp.next_node is not None:
            if tmp.next_node.data >= value:
                break
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new
        
        def __str__(self):
            string = ""
            tmp = self.__head
            while tmp is not None:
                string += str(tmp)
                if tmp.next_node is not None:
                    string += "\n"
                tmp = tmp.next_node
            return string
