class Node:
    def __init__(self, country = None, capital = None):
        self.country = country
        self.capital = capital
        self.next = None
        self.prev = None
        
    def add(self, country, capital):
        if self.country is None:
            self.country = country 
            self.capital = capital
            return self
        newNode = Node(country, capital)
        pointer = self
        while (pointer.next):
            pointer = pointer.next
        pointer.next = newNode
        newNode.prev = pointer
        return newNode
        
myList = Node()
 
while True:
    print("1. Add node")
    print("2. Remove node")
    print("3. list view from left to right")
    print("4. list view from right to left")
    print("5. Does list contain?")
    print("0. Exit")
    
    swt = input()
    
    if swt == '1':        #Add node 
        country = input("Country: ")
        capital = input("Capital: ")
        
        myList = myList.add(country, capital)
        
    elif swt == '2':    #Remove node
        rmNode = input("Enter a country: ") 
        chain = myList
        while rmNode != chain.next.country:
            chain = chain.next
        chain.next = chain.next.next
    
    elif swt == '3':    #List view l-to-r
        chain = myList
        if chain.country is None:
            print("A hde? A net\n")
        else:
            while chain.next:
                print(chain.country, chain.capital)
                chain = chain.next
            
    elif swt == '4':    #List view r-to-l
        chain = myList
        if chain.country is None:
            print("A hde? A net\n")
        else:
            while chain:
                chain = chain.next
            while chain:
                chain = chain.prev
                print(chain.country, chain.capital)
    
    elif swt == '5':    #Does list contain
        search = input("Enter a country: ")
        chain = myList
        while chain.next:
            chain = chain.next
            if chain.country == search:
                print("Yea")
                break
            if chain.next == None:
                print("Nea")
    
    else:
        break







