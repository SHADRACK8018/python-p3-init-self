#!/usr/bin/env python3

class Dog:
    # __init__ method to initialize name and breed attributes
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

    # Instance method for barking
    def bark(self):
        print("Woof!")
