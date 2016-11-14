word = input()
text = []
while word:
    text.append(word)
    word = input()
for i in range(len(text)):
    new = text[i]
    new = new[::-1]
    new = list(new)
    for t in range (len(new)):
        if (t + 1) % 3 == 0:
            new[t] = ''
    wrd = ''.join(new)
    print(wrd)
