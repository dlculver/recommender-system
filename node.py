class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node
## we need to override str so that we can use the command stringify_list in linked list
    ## otherwise it will only return the location of the nodes, and not their values
    def __str__(self):
        return str(self.value)