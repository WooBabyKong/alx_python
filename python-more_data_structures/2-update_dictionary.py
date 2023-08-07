#!/usr/bin/python3
update_dictionary = __import__('2-update_dictionary').update_dictionary

def print_sorted_dictionary(my_dict):
    """ Print sorted dictionary """
    keys = sorted(my_dict.keys())
    for k in keys:
        print("{}: {}".format(k, my_dict[k]))


my_dict = { 'a': "a", 'b': "b" , 'c': "c", 'd': "d", 'e': "e" }
key = "a"
value = "A"
new_dict = update_dictionary(my_dict, key, value)
print_sorted_dictionary(new_dict)
print("xx")
print_sorted_dictionary(my_dict)