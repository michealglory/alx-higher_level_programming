#!/usr/bin/python3
"""
This module defines a base class for other classes to inherit from.
It includes utility functions for working with JSON and CSV data,
as well as a function to draw rectangles and squares using the turtle module.
"""


import csv
import json
import os
import turtle


class Base:
    """
    Represents the base class for all other classes created.

    Attributes:
        id (int): An identifier for the instance.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance with an optional identifier.

        Args:
            id (int): An optional identifier for the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries to be converted
            to JSON.

        Returns:
            str: A JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or not
                all(type(i) == dict for i in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a JSON representation of a list of objects to a file.

        Args:
            list_objs (list): A list of objects to be serialized and saved
            to a file.
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string to a list of JSON string representations.

        Args:
            json_string (str): A JSON string to be converted.

        Returns:
            list: A list of JSON string representations.
        """
        json_string_list = []

        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            json_string_list = json.loads(json_string)

        return json_string_list

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance of a class with attributes set from a dictionary.

        Args:
            **dictionary: Keyword arguments representing object attributes.

        Returns:
            object: An instance of the class with attributes set.
        """
        # create an instance of an existing class
        if cls.__name__ == 'Rectangle':
            temp = cls(1, 1)
        elif cls.__name__ == 'Square':
            temp = cls(1)

        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of instances from a JSON file.

        Returns:
            list: A list of instances of the class.
        """

        json_file = cls.__name__ + ".json"
        instance_list = []
        dict_list = []

        if os.path.exists(json_file):
            with open(json_file, 'r') as my_file:
                read_str = my_file.read()
                dict_list = cls.from_json_string(read_str)
                for dictionary in dict_list:
                    instance_list.append(cls.create(**dictionary))
        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes a list of objects to CSV format and saves them to a file.

        Args:
            list_objs (list): A list of objects to be serialized and
            saved in CSV format.
        """

        # if (type(list_objs) != list and list_objs is not None
        #    or not all(isinstance(i, cls) for i in list_objs)):

        #     raise TypeError("list_objs must be a list of instances")

        # file_name = cls.__name__ + ".csv"
        # with open(file_name, 'w') as my_file:
        #     if list_objs is not None:
        #         list_objs = [i.todictionary for i in list_objs]
        #         if cls.__name__ == 'Rectangle':
        #             records = ['id', 'width', 'height', 'x', 'y']
        #         elif cls.__name__ == 'Square':
        #             records = ['id', 'size', 'x', 'y']
        #         script = csv.DictWriter(my_file, fieldnames=records)
        #         script.writeheader()
        #         script.writerows(list_objs)

        csv_file = cls.__name__ + ".csv"
        with open(csv_file, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    f_names = ["id", "width", "height", "x", "y"]
                else:
                    f_names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=f_names)
                for object in list_objs:
                    writer.writerow(object.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes CSV data from a file and returns a list of instances.

        Returns:
            list: A list of instances of the class.
        """

        # file_name = cls.__name__ + ".csv"
        # list_of_instances = []
        # if os.path.exists(file_name):
        #     with open(file_name, 'r') as my_file:
        #         reader = csv.reader(my_file, delimiter=',')
        #         if cls.__name__ == 'Rectangle':
        #             records = ['id', 'width', 'height', 'x', 'y']
        #         elif cls.__name__ == 'Square':
        #             records = ['id', 'size', 'x', 'y']
        #         for i, row in enumerate(reader):
        #             if i > 0:
        #                 x = cls(1, 1)
        #                 for j, y in enumerate(row):
        #                     if y:
        #                         setattr(x, records[j], int(y))
        #                 list_of_instances.append(x)
        # return list_of_instances

        csv_file = cls.__name__ + ".csv"
        try:
            with open(csv_file, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    f_names = ["id", "width", "height", "x", "y"]
                else:
                    f_names = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=f_names)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draws rectangles and squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        rec_turt = turtle.Turtle()
        rec_turt.screen.bgcolor("#b7312c")
        rec_turt.pensize(3)
        rec_turt.shape("turtle")

        rec_turt.color("#ffffff")
        for rect in list_rectangles:
            rec_turt.showturtle()
            rec_turt.up()
            rec_turt.goto(rect.x, rect.y)
            rec_turt.down()
            for i in range(2):
                rec_turt.forward(rect.width)
                rec_turt.left(90)
                rec_turt.forward(rect.height)
                rec_turt.left(90)
            rec_turt.hideturtle()

        rec_turt.color("#b5e3d8")
        for sq in list_squares:
            rec_turt.showturtle()
            rec_turt.up()
            rec_turt.goto(sq.x, sq.y)
            rec_turt.down()
            for i in range(2):
                rec_turt.forward(sq.width)
                rec_turt.left(90)
                rec_turt.forward(sq.height)
                rec_turt.left(90)
            rec_turt.hideturtle()

        turtle.exitonclick()
