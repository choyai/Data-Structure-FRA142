from Node import Node
from Queue import Queue

def FindX (Slot):
    if len(Slot) == 2 :
        x = int(Slot[0])
        return x
    else:
        print ("Unknown slot input")
def FindY (Slot):
    if len(Slot) == 2 :
        y = int(Slot[1])
        return y
    else:
        print ("Unknown slot input")

def CheckAvai (x,y):
    if Warehouse1[x][y] == None:
        return True
    else:
        return False

def CheckBeltAvai():
    return belt.size < 10

def executeCommand(Command):
    Command = Command.lower()
    if len(Command) == 0: #this is a quick fix to avoid index range errors
        Command = " "
    if Command[0] in ['0','1','2','3','4','5','6','7','8','9']:
        #Check for each command
        if Command[0] == '0':
            ID = Command[1:5]
            Row = Command[2]
            Slot = Command[3:5]
            x = FindX(Slot)
            y = FindY(Slot)
            if CheckAvai(x, y) == False:
                if CheckBeltAvai() == True:
                    belt.add(Node(Warehouse1[x][y]))
                    Warehouse1[x][y] = None
                    print("Getting product ID: " + ID + " from slot number " + Slot)
                    print("Placing product ID: " + ID + " on the belt")
                else:
                    print("Conveyor belt is full. Cannot place the product")
            else:
                print("Cannot find the product")

        elif Command[0] == '1':
            ID = Command[1:5]
            Row =Command[2]
            Slot = Command [3:5]
            x =FindX(Slot)
            y = FindY(Slot)
            if CheckAvai(x, y) == True:
                Warehouse1 [x][y] = ID
                print ("Storing product: " + ID + "In slot number " + Slot)
                print ("Stored successfuly")
            else:
                print("Slot is occupied. Cannot store the product.")

        elif Command[0] == '2':
            print("a")

        elif Command[0] == '3':
            if  belt.size != 0:
                print("Retrieving product with ID: " + belt.remove() + " from the belt.")
                print("There are now " + str(belt.size) + " products on the belt.")
            else:
                print("No products to retrieve!")

        elif Command[0] == '4':
            print ("Warehouse A")
            print("row 1")
            txt = "products in row1 :"
            count = 0
            for x in range(10):
                for y in range(10):
                    if Warehouse1 [x][y] != None:
                        txt = txt + " A1" + str(x) + str(y) +"  "
                        count +=1
            print (txt)
            print ("Total products: " + str(count))

        elif Command[0] == '5':
            Print("a")

        elif Command[0] == '6':
            Print("a")

        elif Command[0] == '7':
            Print("a")

        elif Command[0] == '8':
            Print("a")

        elif Command[0] == '9':
            ID = Command[1:5]
            Row = Command[2]
            Slot = Command[3:5]
            NewID = Command[5:9]
            Row = Command[6]
            NewSlot = Command[7:9]
            x = FindX(Slot)
            y = FindY(Slot)
            newx = FindX(NewSlot)
            newy = FindY(NewSlot)
            if CheckAvai(x, y) == False:
                if CheckAvai(newx, newy) == False:
                    print("Slot is occupied. Failed to move.")
                else:
                    Warehouse1[newx][newy] = Warehouse1 [x][y]
                    Warehouse1[x][y] = None
                    print("Moved product ID: " + ID + " to " + NewID)
            else:
                print("Slot is empty. Failed to move.")

    else:
        print ("Incorrect command syntax")
    print ("\n -------------------------------------------------------------------- \n")

#Initialization

Warehouse1 = [[None for x in range(10)] for y in range(10)]
print ("Warehouse1 Generated")
belt = Queue()
commandQue = Queue()

#Input

print ("Conveyor Belt Generated")
print ("Input your commands")
print (" 0XXXX \n"
       "Retrieve a product with ID XXXX \n"
       "1XXXX \n"
       "Store a product with ID XXXX \n"
       "2XY00 \n"
       "Sort warehouse X at row Y \n"
       "30000 \n"
       "Retrieve a product from the conveyor belt \n"
       "40000 \n"
       "Output information on all of the warehouses \n"
       "5XXXX \n"
       "Search for a product ID XXXX \n"
       "9XXXXYYYY \n"
       "Manually put a product ID XXXX at position YYYY \n")
newcom = True
while newcom:
    comm = input("Please enter command\n")
    commandQue.add(Node(comm))
    yesno = ''
    while yesno != 'y' and yesno != 'n':
        yesno = input("Would you like to enter another command? y/n\n")
        yesno = yesno.lower()
    if yesno == 'n':
        newcom = False
#Execution
for i in range(commandQue.size):
    executeCommand(commandQue.remove())
