import re
import os

def folders():
    counter = 0
    numbers = '[0-9]'
    titles = os.listdir('.')
    for i in titles:
        if os.path.isdir(i) and re.search (numbers, i):
            counter += 1
    return str(counter)

def names():
    print('Все файлы и(или) папки в текущей папке: ')
    arr = []
    res = '\..+'
    for i in os.listdir('.'):
        name = i
        if os.path.isdir(i):
            name = re.sub(res, '', i)
        if name not in arr:
            arr.append(name)
    for each in arr:
        if each:
            print(each + '\n')
        else:
            print('None')

print('Количество папок с цифрами в названии в текущей папке: ' + folders())
names()

            
        
            
