from Node import Node


class tree:
    def __init__ (self):
        self.root= None
    def add(self,data):
        if self.root == None:
            self.root = Node(data)
            print ("Root has been added")
            treelevel = 1
        else:
            temp = self.root
            a = True
            while(a == True ):
                if data < temp.name:
                    if temp.previous != None:
                        temp = temp.previous
                        #print ("find l")
                    else:
                        temp.upper = temp
                        temp.previous = Node(data)
                        print (str(temp.upper.name))
                        #print ("left ----")
                        print("Leaf has been added P")
                        a = False
                elif data > temp.name:
                    if temp.next !=None:
                        temp = temp.next
                        #print("find r")
                    else:
                        temp.upper = temp
                        temp.next = Node(data)
                        print(str(temp.upper.name))
                        #print("right ----")
                        print("Leaf has been added N")
                        a = False
                else:
                    print("Can't add data")
                    break

    def delete (self, data):
        temp = self.root
        b =True
        btemp = self.root
        dir = ""
        while (b == True):
            if data == self.root.name:                       #delete root

                if (temp.previous.name != None) and (temp.next.name != None):
                    cc = temp.previous
                    self.root = temp.next
                    self.root.previous = cc
                    print("path 0")
                    b = False
                elif root.next.name != None:
                    self.root = temp.next
                    print("path 2")
                    b = False
                elif self.root.previous.name != None:
                    self.root = temp.previous
                    print("path 1")
                    b= False
                else:
                    self.root = None
                    print("path 3")
                    b = False
            elif data < temp.name:
                btemp = temp
                temp = temp.previous
                dir = 'l'
            elif data > temp.name:
                btemp = temp
                temp = temp.previous
                dir = 'r'
            elif data == temp.name:
                upper = temp.upper
                if (temp.previous.name != None) and (temp.next.name != None):
                    if dir == 'l':
                        temp.next.upper = upper
                        #upper.previous= temp.next
                        btemp.previous = temp.next
                        temp.next.previous = temp.previous
                        temp.next.previous.upper = temp.next
                        temp = None
                    elif dir == 'r':
                        temp.next.upper = upper
                        #upper.next = temp.next
                        btemp.next = temp.next
                        temp.next.previous = temp.previous
                        temp.next.previous.upper = temp.next
                        temp = None
                    print("path 4")
                    b = False
                elif temp.previous.name != None:
                    temp.previous.upper = upper
                    ram = temp.previous
                    print("path 5")
                    b = False
                elif temp.next.name != None:
                    temp.next.upper = upper
                    ram = temp.next
                    print("path 6")
                    b = False






class main:
    t=tree()
    t.add(10)
    t.add(6)
    t.add(12)
    t.add(14)
    t.add(7)
    t.delete(10)
    t.add(13)
    t.add(3)
    t.add(10)
    t.add(2)
    t.add(5)
    t.delete(3)
    t.add(3)
    t.add(4)



