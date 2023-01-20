perona = [0,] * 1500

def hash_brown(fam):
    return ord(fam[0]) * 9

def add_to(fam, dr, hob1, hob2, hob3, hob4):
    perona[hash_brown(fam[0])] = [fam, dr, hob1, hob2, hob3, hob4]

def to_file():
    with open('bimbam.txt', 'wt') as file:
        for i in range(1500):
            if perona[i] != 0:
               for element in perona[i]:
                    file.write(element + ' ')
               file.write('\n')
while True:
    print("1. Add")
    print("2. Search")
    print("3. View")
    print("0. Exit")
    
    swt = input()
    
    if swt == '1':        #Add node 
        fam = input("fam: ")
        dr = input("dr: ")
        hob1 = input("hob1: ")
        hob2 = input("hob2: ")
        hob3 = input("hob3: ")
        hob4 = input("hob4: ")
        
        add_to(fam, dr, hob1, hob2, hob3, hob4)
        to_file()
        
    elif swt == '2':    #Search
        sch = input("fam: ")
        print(perona[hash_brown(sch)])
        
    elif swt == '3':    #Search
        for i in range(1500):
            if perona[i] != 0:
                print(perona[i])
        
    else:
        break
    
