import os

a = {}

def dict_new():
    for root, dirs, files in os.walk('.\\news'): ## папка "news" находится в текущей папке, то есть '.\\news'
        for file in files:
            with open (os.path.join(root, file), 'r', encoding = 'cp1251') as page:
                raw_text = page.read()
                a[file] = raw_text.count('<se') ## считает все тэги с предложениями
    create_file(a)


def create_file(dictionary):
    with open('task 1(sentences).txt', 'w', encoding = 'utf-8') as text_file: 
        for key in a:
            line = key + '\t' + str(a[key]) ## записывает в строку данные с табуляцией и переходом на другую строку
            text_file.write(line  + '\n')

def main():
    print ('Документ task 1(sentences).txt создан.')
    dict_new()

if __name__ == '__main__':
    main()
    
