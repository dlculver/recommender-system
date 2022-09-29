## root file = recommender.py

from node import Node

class LinkedList:
    def __init__(self, value = None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, value):
        current_head = self.get_head_node()
        new_head = Node(value)
        new_head.set_next_node(current_head)
        self.head_node = new_head

    def stringify_list(self):
        string = ''
        current_node = self.head_node
        while current_node:
            string_list += str(current_head.value) + "\n"
            current_node = current_node.get_next_node()
        return string

    def remove_node(self, value_to_remove):
        current_node = self.head_node
        if self.head_node.get_value() == value_to_remove:
            self.head_node = self.head_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else: current_node = next_node
