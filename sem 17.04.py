# import os
# tree = os.walk('.')
# print (tree)

# for root, dirs, files in os.walk(r'Desktop\2539\CORPUS_TXT'):
#     for f in files[:300]:
#         with open(os.path.join(root,f), 'r', encoding = 'utf-8') as text:
#             whole_corpus += text.read()
# len(whole_corpus.split(' '))
      
# for root, dirs, files in os.walk('.', topdown=False):   
#     print(root)

# for root, dirs, files in os.walk('.'):
#     for d in dirs:
#        if d.starswith('.'):
#            dirs.remove(d)


# Задачи
# 1
# def delete_folders(path):
#     for root, dirs, files in os.walk(path, topdown = False):
#         for f in files:
#             os.remove(os.path.join(root,f))
#         for d in dirs:
#             os.rmdir(os.path.join(root,d))
#     os.rmdir(path)
#     print('Done!')
# delete_folders(r'Desktop\21')

# 2
# def separation():
#     for root, dirs, files in os.walk('.'):
        # считаем сколько бэкслэшей
#         num = root.count('\\')
#         root = root.split('\\')[-1]
#         print('\t'*(num),root, sep = '--')
#         for f in files:
#             print('\t'*(num +1),f)
# separation()
        
