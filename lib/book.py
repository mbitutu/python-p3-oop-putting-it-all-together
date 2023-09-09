#!/usr/bin/env python3

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


    def title(self):
        return self.title

    def author(self):
        self.author


    def pages(self):
        return self.pages


    def pages(self, pages):
        if pages > 0:
            self.pages = pages
        else:
            print("Invalid number of pages")


    def get_book_info(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"


    
        