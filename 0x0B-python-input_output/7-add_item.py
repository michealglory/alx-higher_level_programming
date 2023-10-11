#!/usr/bin/python3
"""This script adds command-line arguments to a list stored in a JSON file.
If the file does not exist, it creates one and initializes an empty list."""


import sys


if __name__ == "__main__":
    save_to_json = __import__('5-save_to_json_file').save_to_json_file
    load_from_json = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        item_list = load_from_json("add_item.json")
    except FileNotFoundError:
        item_list = []
    item_list.extend(sys.argv[1:])
    save_to_json(item_list, "add_item.json")
