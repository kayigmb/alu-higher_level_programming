#!/usr/bin/python3
"comment"


class Student:
    "comment"

    def __init__(self, first_name, last_name, age):
        "comment"
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        "comment"
        if attrs is None:
            return self.__dict__
        new_data = {}

        for i in attrs:
            try:
                new_data[i] = self.__dict__[i]
            except Exception:
                pass
        return new_data

    def reload_from_json(self, json):
        "comment"
        for i in json:
            self.__dict__.update({i: json[i]})
