#!/usr/bin/env python3

class Person:
    # __init__ method to initialize the name attribute
    def __init__(self, name):
        self.name = name

    # Instance method for talking
    def talk(self):
        print("Hello World!")

    # Instance method for walking
    def walk(self):
        print("The person is walking.")
