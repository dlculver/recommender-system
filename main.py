from node import Node
import csv

## code to create linked list of the types

types = ['ethics','metaphyics','aesthetics', 'epistemology','political philosophy','philosophy of science','philosophy of mathematics', 'philosophy of language', 'existentialism']

def insert_phil_types():
    phil_types_ll = LinkedList()
    for type in types:
        current_node = Node(type)
        phil_types_ll.insert_beginning(current_node)
    return phil_types_ll

## we want to create a linked list of linked lists, there will be a node for each type
## and the value of the node will be a linked list of all the works that fall under that types

## first we must convert the csv into a list of lists
with open('phil_books.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    phil_books = list(csv_reader)

## the output of the above isn't quite what we want, so we will split the strings along ;

for n in range(len(phil_books)):
    phil_books[n] = phil_books[n][0].split(';')

#print(phil_books)

def insert_book_data():
    phil_book_data_ll = LinkedList()
