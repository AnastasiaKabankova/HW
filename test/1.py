with open('freq.txt', 'r', encoding = 'utf-8') as freq:
    lines = freq.readlines()
    for line in lines:
        word = line.split('|')
        for i in word:
            if i.endswith('союз '):
                print(line)
