# Статья "комар", заменить "комар" на "слон"

import re

def open_read():
    with open('Mosquitoes.html', 'r', encoding = 'utf-8') as f:
        file = f.read()
    return file

def changes(file):
    reg1 = r'\b\комар(а(ми?|х)?|о(м|в)|у|е|ы)?\b'
    reg2 = r'\b\Комар(а(ми?|х)?|о(м|в)|у|е|ы)?\b'
    one = re.sub(reg1, 'слон\\1', file)
    two = re.sub(reg2, 'Слон\\1', one)
    return two

def docs(two):
    with open ('Elephants.html', 'w', encoding = 'utf-8') as doc1:
        doc1.write(two)
    print('Новая wiki-статья о "слонах": Elephants.html')
    with open ('Elephants.txt', 'w', encoding = 'utf-8') as doc2:
        doc2.write(two)
    print('Файл с результатами замены: Elephants.txt')
    

def main():
    docs(changes(open_read()))

main()
