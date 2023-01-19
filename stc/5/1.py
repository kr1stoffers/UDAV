import matplotlib.pyplot as plt
from random import randint 

perona = [0,] * 2000

ycheck = [0,] * 2000    
xcheck = [0,] * 2000
for i in range(2000):
    xcheck[i] = i + 1

def hash_brown(fio):
    fio.lower()
    return (ord(fio[0]) - 1071) * 60 + (ord(fio[0]) - 1071) - 61

with open('prumrum.txt', 'wt') as file:
    for i in range(2000):
        rand_str = chr(randint(1072, 1103)) + chr(randint(1072, 1103)) + chr(randint(1071, 1103))
        if perona[hash_brown(rand_str)] != 0:
            ycheck[hash_brown(rand_str)] += 1
            file.write(rand_str + '\n')
        else:
            perona[hash_brown(rand_str)] = rand_str
            file.write(rand_str + '\n')
    
plt.xlabel('Ключи')
plt.ylabel('Коллизии')
plt.minorticks_on()
plt.grid(True)

plt.plot(xcheck, ycheck)

line = [1,] * 2000
start = [0,] * 2000
for i in range(0, 2000):
    start[i] = i + 1
plt.plot(start, line, 'r')
plt.title('Плоха',color='red')
plt.show()


