import re

file_name = input('Введите название файла с расширением: ')
app = []

def opentext(file_name):
    with open(file_name,'r', encoding = 'utf-8') as f:
        text = f.read().lower()
        words = text.split(' ')
        for word in words:
            word = word.strip('\n,.;:""''()?![]{}\|/')
            app.append(word)
    return app

reg = r"\b\откр(о|ы)(л(а|о|и)?|(е(шь|те?|м)|ют?)|(й(те)?)|(в(ш(и(й|е|ми?|х)|е(го|му?|й|е)|ую|ая))?|т(ы(й|ми?|х|е)|о(му?|й|е|го)|ую|ая)))(сь|ся)?\b"
new_list = []

def forms(reg):
    words = opentext(file_name)
    for w in words:
        m = re.search(reg, w)
        if m != None:
            new_list.append(w)
    return new_list


print('В данном файле есть следующие формы глагола "открыть":', *forms(reg))
