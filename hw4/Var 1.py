t = input()
while t:
    for index, letter in enumerate (t):
        if letter != 'к' and letter != 'а' and index % 2 == 1:
            print (letter)
    t = input()
