#!/usr/bin/python3
'''Module for Base class.'''


class Base:
    '''A representation of the base of our OPP hierarchy.'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Jsonifies a dictionary so it's quite rightlyy and longer.'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)


    @staticmethod
    def from_json_string(json_string):
        '''Unjsonifies a dictionary.'''
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def load_from_file(cls):
        '''Loads string from file and unjsonifies.'''
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Saves object to csv file.'''
        from models.rectangle import Rectangle
        from models.sqaure import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                            for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                            for o in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w' newline='',
                encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''Loads object to csv file.'''
        from models.rectangle import Rectangle
        from models.sqaure import Square
        ret = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                        "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                        "x": row[2], "y": row[3]}
                ret.append(cls.create(**d))
        return ret

    @staticmethod
    def draw(list_rectangles, list_square):
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for i in list_rectangles + list_sqaures:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))
            t.pensize(10)
            t.forward(i.width)
            t.left(90)
            t.forawrd(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.end_fill()

        time.sleep(5)
