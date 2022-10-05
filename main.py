from node import Node
from linkedlist import LinkedList
import csv

## code to create linked list of the types

types = ['ethics','metaphysics','aesthetics', 'epistemology','political philosophy','philosophy of science','philosophy of mathematics', 'philosophy of language', 'existentialism']
types.sort()


def insert_phil_types():
    phil_type_list = LinkedList()
    for type in types:
        phil_type_list.insert_beginning(type)
    return phil_type_list


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
    see_types = str(input("Would you like to see a list of the types we have data on? \n[y/n]: "))
    valid_responses = ['y','n']
    while see_types not in valid_responses:
        str(input("Please enter [y/n]: "))
    if see_types == 'y':
        for type in types:
            print(type)
    if see_types == 'n':
        pass


# ## worried that str might not work with the sublists in the phil_book_data_ll
#
# sublist = phil_book_data_ll.stringify_list()
# print(sublist)
#
# phil_type_head_node = phil_types_ll.get_head_node()
# print(phil_type_head_node.get_value())







welcome()

## now we will elicit input from the user

selected_phil_type = ''

## code for interaction with user here

while len(selected_phil_type) == 0:
    usr_input = str(
        input(
            "\nWhat kind of philosophy book would you like to read? \nType the beginning of that type of philosophy to see if it is here.\n"
        )
    )

    ## search for user_input in philosophy types data structure

    matching_list = []
    type_list_current_node = my_phil_types.get_head_node()
    while type_list_current_node is not None:
        if str(type_list_current_node.get_value()).startswith(usr_input):
            matching_list.append(type_list_current_node.get_value())
        type_list_current_node = type_list_current_node.get_next_node()



    ## print types of matching philosophy

    print("The following options are types of philosophy which start with what you typed in: ")

    for phil_type in matching_list:
        print(str(phil_type))


    # if there was only one option, then we can return the books we have data on

    if len(matching_list) == 1:
        select_type = str(input(
            "\nThe only matching type for the specified input is " + matching_list[0] + ". \nIs this the what you want to look at? Please enter [y/n]: "))

        ## after getting the philosophy topic, we print out the data

        if select_type == 'y':
            selected_phil_type = matching_list[0]
            print("Selected philosophy topic: " + selected_phil_type)
            phil_list_head = my_phil_books.get_head_node()
            while phil_list_head.get_next_node() is not None:
                sublist_head = phil_list_head.get_value().get_head_node()
                if sublist_head.get_value()[0] == selected_phil_type:
                    while sublist_head.get_next_node() is not None:
                        print("---------------------------")
                        print("Name: " + sublist_head.get_value()[1])
                        print("Author: " + sublist_head.get_value()[2])
                        print("---------------------------")
                        sublist_head = sublist_head.get_next_node()
                phil_list_head = phil_list_head.get_next_node()

            # Ask user if they would like to search for other types of restaurants
            repeat_loop = str(
                input("\nDo you want to find other philosophy books? Enter y for yes and n for no.\n")).lower()
            if repeat_loop == 'y':
                selected_phil_type = ""
            elif repeat_loop == 'n': print("Goodbye! Happy reading! :)")








