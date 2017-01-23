print('Попробуйте отгадать слова по подсказкам!')

with open('fclues.csv', 'r', encoding = 'utf-8') as f:
    lines = f.readlines()


def open_file():
    d = dict()
    for words in lines:
        words = words.strip('\n')
        words = words.split(',')
        value = words[0]
        key = words[1]
        d[value] = key
    return d


def clues(d):
    for value in d:
        print('Подсказка:', d[value])
        attempt(value)
        print()


def attempt(value):
    number = len(value)
    while number != 0:
        guess = input('Введите слово: ')
        if guess == value:
            print('Ура!')
            break
        else:
            print('Боюсь, надо попробовать ещё раз... ')
            number -= 1
    if number == 0:
        print('К сожалению, Вы не смогли отгадать слово.')


clues(open_file())



        
        
