class Node:
    def __init__(self, name = None, next = None, previous = None, upper = None):
        self.name = name
        self.next = next
        self.previous = previous
        self.upper = upper
    def __str__(self):
        return str(self.name)
    def delete(self):
        self.name = None
        self.previous.next = self.next
