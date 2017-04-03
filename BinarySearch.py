from LinkedList import LinkedList
from Node import Node
from Queue import Queue
import random

def BubbleSort(list_linked):
    done = False
    while done == False:
        swap = False
        for i in range(list_linked.size - 1):
            item = list_linked.head
            for n in range(i):
                item = item.next
            if item.name > item.next.name:
                temp = item.name
                item.name = item.next.name
                item.next.name = temp
                swap = True
        if swap == False:
            done = True
            it = list_linked.head
            print(it)
            for i in range(list_linked.size):
                it = it.next
                print(it)

    return list_linked

def BinarySearch(list_linked, item):
    lb = 1
    ub = list_linked.size
    found = False
    while found == False:
        if ub < lb:
            print("Data not found.")
            return None
            break
        mid = int(lb + (ub - lb)/2)
        temp = list_linked.head
        for i in range(mid):
            temp = temp.next
        if temp.name == item:
            print("Found data " + str(item) + " at position " + str(mid + 1))
            found = True
            return mid
            #print("e2")
        if temp.name < item:
            lb = mid + 1
            print("e3")
        if temp.name > item:
            ub = mid - 1
            print("e4")

qu = Queue()
for i in range(100):
    qu.add(Node(random.randint(1, 100)))

BubbleSort(qu)
BinarySearch(qu, 5)
