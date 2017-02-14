def open_read():
    num = 0
    with open('F.xml', 'r', encoding = 'utf-8') as f:
        lines = f.readlines()
        for line in lines:
            num += 1
    return num

def write_doc(num):
    numlines = str(num)
    with open ('Number.txt', 'w', encoding = 'utf-8') as new_doc:
        new_doc.write(numlines)
        print('Количество строк: ' + numlines + '\n' + 'Создан документ Number.txt')

def main():
    write_doc(open_read())

main()

