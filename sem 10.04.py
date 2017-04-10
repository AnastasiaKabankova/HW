#Работа с файлами и папками
#Модули os, shutil

import os
import shutil

#with open(f) кодировка по умолчанию
#В Windows Windows C:\\Users\\student\\Downloads
#На MAC и Linux /home/student/Downloads

#Текущая папка обозначается точкой
#os.path.abspath('.')
#'C:\\Users\\student'
#os.getcwd()
#'C:\\Users\\student'
#os.path.join('texts','1.txt')
#f = 'texts\\1.txt'

#' '.join(['hello', 'world']) --> hello world
#os.path.exists('texts') --> True
#os.listdir('.') говорит, что лежит в текущей папке
#s = 'Hello'
#i = 1
#texts = [open(f)

#os.mkdir('corpus')

#Преименовать папку или файл
#os.rename('corpus', 'new_corpus')переменные: старый путь к файлу, новый путь к файлу 

#os.path.isdir('

#poshutil.#when you just can't cope

#shutil.copy(r'texts\corpus1.txt', r'new_corpus\corpus1.txt)
#shutil.copetree('texts', 'corpus')
#shutil.move('text', 'a')

#Питон опасный, удаляет папки навсегда

#os.remove(r'corpus\corpus2.txt') удалить файл 'corpus2.txt' из папки 'corpus')
#shutil.rmtree('a')

#1
#sent = input('Введите предложение на английском языке без знаков препинания: ')
#words = sent.replace(' ','\\')
#os.makedirs(words)

#2 (тут что-то не тааак)
#number = int(input('Введите число: '))
#for i in range(1, number + 1):
#    os.mkdir(str(i))
#    for j in range(i):
#        open(str(j), 'w')
       



