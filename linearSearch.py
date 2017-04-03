from LinkedList import LinkedList
from Node import Node

def linearSearch(list_linked, item):
    temp = list_linked.head
    for i in range(list_linked.size):
        if temp.name == item:
            print("Found data at position " + str(i))
            return str(i)
        temp = temp.next
    print("Data not found.")
    return None

linked = LinkedList()
