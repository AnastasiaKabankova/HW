import os

def depth():
    great = []
    for root, dirs, files in os.walk('.', topdown = False):
        number = root.count('\\')
        great.append(number)
    print('Максимальная глубина папки в этом древе: ' + str(max(great)))
    
depth()
            
        
