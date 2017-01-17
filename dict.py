d = {"Россия":'Москва',
     "Польша":'Варшава',
     "США":'Вашингтон',
     "Болгария":'София',
     "Армения":'Ереван',
     "Бразилия":'Бразилиа',
     "Испания":'Москва'}
#for key in d:
#    print(key + ' * ' + d[key])

#def capital():
#    r = input('Введите название страны: ')
#    if r in d:
#        print(d[r])
#    else:
#        print('Такой страны здесь нет')
#    return d[r]
#capital()

#def revert(d):
#    for key in d:
#        print(d[key] + ' - ' + key)
#revert(d)

def delete_doubles(d):
    arr = []
    new = {}
    for key in d:
        if d[key] in arr:
            
        else:
            new[key] = key
            arr.append(d[key])
    return a
delete_doubles(d)
    
            
