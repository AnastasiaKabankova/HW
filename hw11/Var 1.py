file_name = input('Введите название файла с расширением: ')
def opentext(file_name):
    with open(file_name,'r', encoding = 'utf-8') as f:
        text = f.read()
        text = text.lower()
        word = text.split(' ')
        for i, lex in enumerate(word):
            word[i] = lex.strip('.,!?/:;()[]"0123456789-')
    return word

def word_ing(a):
    a = opentext(file_name)
    k = 0
    for element in a:
        if element.endswith('ing'):
            k += 1
    return k

new_word = input('Введите слово, заканчивающееся на -ing: ')
def form_ing(a, new_word):
    a = opentext(file_name)
    d = 0
    for element in a:
        if element == new_word:
            d += 1
    return d
end = opentext(file_name)
print('Количество слов в данном тексте, которые заканчиваются на -ing:', word_ing(end))
print('Столько раз в данном тексте встречается форма, введённая пользователем:', form_ing(end, new_word))
            
