class Node:
    def __init__(self, name = None):
        self.name = name
        self.prev = None
        self.next = None
    
    tail = None
    def add(self, name):
        if self.name is None:
            self.name = name
            return self
        self.tail = Node(name)
        pointer = self
        while (pointer.next):
            pointer = pointer.next
        pointer.next = self.tail
        self.tail.prev = pointer
        return self
    def remove(self):
        if self.next is None:
            self.name = None
            return self
        self = self.next
        self.prev.next = None
        self.prev = None
        return self

myList = Node()
counter = 0

while True:
    print("1. Add node")
    print("2. Remove node")
    print("3. list view")
    print("4. Counter of elements")
    print("5. Does list contain?")
    print("0. Exit")
    
    swt = input()
    
    if swt == '1':        #Add node 
        name = input("Name: ")
        
        myList = myList.add(name)
        counter += 1
        
    elif swt == '2':    #Remove node
        myList = myList.remove()
        
        counter -= 1
    
    elif swt == '3':    #List view
        chain = myList
        if chain.name is None:
            print("A hde? A net\n")
        else:
            while chain:
                print(chain.name)
                chain = chain.next
            
    elif swt == '4':    #Count of elements
        print('count of elements: ', counter)
    
    elif swt == '5':    #Does list contain
        search = input("Enter a name: ")
        chain = myList
        while chain:
           
            if chain.name == search:
                print("Yea")
                break
            if chain.next == None:
                print("Nea")
                break
            chain = chain.next
    
    else:
        break
    
    
    
    
   
  
  # yamete kudasai
