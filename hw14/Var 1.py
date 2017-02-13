import re

def open_read():
    with open(input('Введите название файла с расширением: '), 'r', encoding = 'utf-8') as f:
        text = f.read()
    return text

def capital(text):
    cap = re.search(r'"P36"(.*?)<a href=(.*?)>(.*?)</a>', text, flags = re.DOTALL) #находит то, что содержится именно в самой карточке (infobox)
    cap = cap.group(3)
    return cap

def write_doc(cap):
    with open ('Capital.txt', 'w', encoding = 'utf-8') as new_doc:
        new_doc.write(cap)
        print('Столица данной страны: ' + cap + '\n' + 'Создан документ Capital.txt')
       
def main():
    write_doc(capital(open_read()))

main()
