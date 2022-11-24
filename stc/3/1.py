class Node:
    def __init__(self, name = None, fac = None, cours = None, group = None):
        self.name = name
        self.fac = fac
        self.cours = cours
        self.group = group
        self.next = None
        
    def add(self, name, fac, cours, group):
        newNode = Node(name, fac, cours, group)
        pointer = self
        while (pointer.next):
            pointer = pointer.next
        pointer.next = newNode
    

myList = Node()

while True:
    print("1. Add node")
    print("2. Remove node")
    print("3. List view")
    print("4. Does list contain?")
    print("0. Exit")
    
    swt = input()
    
    if swt == '1':        #Add node 
        name = input("Name: ")
        fac = input("Faculty: ")
        cours = input("Cours: ")
        group = input("Group: ")
        
        myList.add(name, fac, cours, group)
        
    elif swt == '2':    #Remove node
        rm = input("Enter a node: ")
        chain = myList
        while chain.next:
            chain = chain.next
            key = chain.name + " " + chain.fac + " " + chain.cours + " " + chain.group
            if key == rm:
                pass
    
    elif swt == '3':    #List view
        chain = myList
        while chain.next:
            chain = chain.next
            print(chain.name, chain.fac, chain.cours, chain.group)
            
    elif swt == '4':    #Does list contain
        search = input("Enter a node: ")
        chain = myList
        while chain.next:
            chain = chain.next
            key = chain.name + " " + chain.fac + " " + chain.cours + " " + chain.group
            if key == search:
                print("Yea")
                break
            if chain.next == None:
                print("Nea")
                
    else:
        break







