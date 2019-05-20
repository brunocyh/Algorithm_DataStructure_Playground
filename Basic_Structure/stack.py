from .interface import Interface

class Stack(Interface):
    """
    Try to implement stack with only primitive structure
    """

    def __init__(self):
        self.lst = []

    def insert(self, text_object):
        self.lst.append(text_object)

    def delete(self):
        self.lst.pop()

    def peek(self):
        return self.lst[-1]

    def is_empty(self) -> bool:
        return len(self.lst) == 0
