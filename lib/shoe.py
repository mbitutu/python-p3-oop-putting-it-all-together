#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, color):
        self.brand = brand
        self.size = size
        self.color = color


    def brand(self):
        return self.brand


    def size(self):
        return self.size


    def size(self, size):
        if size > 0:
            self.size = size
        else:
            print("Invalid shoe size")


    def color(self):
        self.color = color


    def get_shoe_info(self):
        return f"Brand: {self.brand}, Size: {self.size}, Color: {self.color}"
