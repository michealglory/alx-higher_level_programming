#!/usr/bin/python3
"""This module defines a Python function that converts a class instance
into a JSON-compatible dictionary."""


def class_to_json(obj):
    """Returns the dictionary representation of a python data structure"""
    return obj.__dict__
