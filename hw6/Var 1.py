word = input('Введите слово: ')
print(word)
for i in range(len(word)):
    print(word[:-(1+i)])
