perona = [[],] * 1000

def hash_brown(name):
    return (ord(name[0]) + ord(name[1])) % 1000

def add_to(name, sname):
    index = hash_brown(name)
    perona[index] = [name, sname]

def to_file(name):
    with open('a.txt', 'at') as file:
        file.write(str(perona[hash_brown(name)]))
        file.write('\n')

while True:
    print("1. Add")
    print("2. Search")
    print("0. Exit")
    
    swt = input()
    
    if swt == '1':        #Add node 
        name = input("Name: ")
        sname = input("Sname: ")
        
        add_to(name, sname)
        to_file(name)
        
    elif swt == '2':    #Search
        sch = input("Name: ")
        print(perona[hash_brown(sch)])
    
    else:
        break
    
    
    
