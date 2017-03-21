from LinkedList import LinkedList
from Node import Node
from StackClass import StackClass
from Queue import Queue
import datetime

stacki = StackClass()
queue = Queue()
print(str(queue.isEmpty))
print(str(stacki.isEmpty))
#for i in range(10):
    #stacki.push(Node(i))
    #queue.add(Node(i))
    #print(Node(i))
#for i in range(10):
    #print(stacki.pop())
    #print(queue.remove())
linked = LinkedList()
for i in range(10):
    linked.add(Node(i), i)
for i in range(10):
    print(linked.remove(i))
