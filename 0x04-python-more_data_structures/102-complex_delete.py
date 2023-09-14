#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_deleted = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            keys_to_deleted.append(key)
    for key in keys_to_deleted:
        del a_dictionary[key]
    return a_dictionary
