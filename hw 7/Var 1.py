with open('Master and Margarita.txt','r', encoding = 'utf-8') as MM:
    tablewords = []
    space = 0
    lines = MM.readlines()
    print(' ', *lines)
    for i in range(len(lines)):   
        for k in range(len(lines[i])):
            if lines[i][k] == ' ':            
                space += 1
        tablewords.append(space + 1)
        space = 0
    number = 0
    for l in range(len(tablewords)):
        number += tablewords[l]
        averword = number/len(lines)
    print('\n','Среднее количество слов в строке =',averword)                   
                       
        
