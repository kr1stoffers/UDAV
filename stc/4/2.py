perona = [0,] * 1000
check = [0. ] * 1000

def hash_brown(name):
    return (ord(name[0]) + ord(name[1])) % 1000

def add_to(name, sname):
    index = hash_brown(name)
    if perona[index] != 0:
        check[index] += 1
        name_of_file = str(check[index]) + '.txt'
        with open(name_of_file, 'at') as file:
            file.write(name + ' ' + sname + '\n')
    else:
        perona[index] = [name, sname]

def to_file():
    with open('a.txt', 'wt') as file:
        for i in range(1000):
            if perona[i] != 0:
               for element in perona[i]:
                    file.write(element + ' ')
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
        to_file()
        
    elif swt == '2':    #Search
        sch = input("Name: ")
        print(perona[hash_brown(sch)])
    
    else:
        break
    
    
    
