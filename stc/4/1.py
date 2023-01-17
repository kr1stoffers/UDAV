with open('Num.txt', 'wt') as file: #null of file
    for i in range(0, 1000):
        file.write('_')


while True:
    print("1. Add to file")
    print("2. View file")
    print("0. Exit")
    
    swt = input("Your choose: ")
    
    if swt == '1':    #Add to file
        change = int(input("Enter a number: "))
        
        with open('Num.txt', 'rt') as file:
            index = list(file.read())
            
            index[change - 1] = str(change)
            for number in range(0, 550):
                index[number] = '_'
                
            add_to_file = ''.join(index)
            
            
        with open('Num.txt', 'wt') as file:
            file.write(add_to_file)
            
    elif swt == '2':    #View file
        with open('Num.txt', 'rt') as file:
            print(file.read())
    
    else:
        break
