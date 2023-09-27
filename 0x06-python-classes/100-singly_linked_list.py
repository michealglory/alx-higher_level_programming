#!/usr/bin/python3
"""Template of a singly linked list"""


class Node:
    """"defines a node"""

    def __init__(self, data, next_node=None):

        self.data = data
        self.next_node = next_node

    @property
    def data(self):

        return (self.__data)

    @data.setter
    def data(self, value):

        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):

        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must be a Node object')

        self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list"""

    def __init__(self):

        self.head = None

    def __str__(self):

        print_output = ""
        position = self.head
        while position:
            print_output += str(position.data) + "\n"
            position = position.next_node
        return print_output[:-1]

    def sorted_insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return
        position = self.head
        while position.next_node and position.next_node.data < value:
            position = position.next_node
        if position.next_node:
            new_node.next_node = position.next_node
        position.next_node = new_node
