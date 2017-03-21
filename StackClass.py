from LinkedList import LinkedList
class StackClass(LinkedList):
    def __init__(self, size = 0):
        LinkedList.__init__(self, size = None)
    def push(self, node):
        LinkedList.add(self, node, self.size)
    def pop(self):
        if self.size < 1:
            return None
        else:
            temp = self.tail
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.tail = temp.previous
            self.size -= 1
            return temp
