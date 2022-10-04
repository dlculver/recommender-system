from node import Node
from linkedlist import LinkedList
import csv

## code to create linked list of the types

types = ['ethics','metaphyics','aesthetics', 'epistemology','political philosophy','philosophy of science','philosophy of mathematics', 'philosophy of language', 'existentialism']
types.sort()
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

## creating linked list of linked lists, with the each node being a linked list consisting of all books of that particular type


def insert_book_data():
    phil_book_data_ll = LinkedList()
    for phil_type in types:
        phil_type_sublist = LinkedList()
        for book in phil_books:
            if book[0] == phil_type:
                phil_type_sublist.insert_beginning(book)
        phil_book_data_ll.insert_beginning(phil_type_sublist)
    return phil_book_data_ll

my_phil_types = insert_phil_types()
my_phil_books = insert_book_data()

## welcome message for user

def welcome():
    print("Welcome to the philosophy recommender system! \nA tool for finding philosophy books to read by type :)")
    see_types = str(input("Would you like to see a list of the types we have data on? \n[y/n]"))
    valid_responses = ['y','n']
    while see_types not in valid_responses:
        str(input("Please enter [y/n]: "))
    if see_types == 'y':
        for type in types:
            print(type)
    if see_types == 'n':
        pass

welcome()

## now we will elicit input from the user

selected_phil_type = ''
#
# while len(selected_phil_type) == 0:
#     usr_input = str(
#         input(
#             "\nWhat kind of philosophy book would you like to read? \nWould you like to see a list of the types of philosophy to see if its here?.\n"
#         )
#     )

