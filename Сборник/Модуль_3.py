# Задание 1
"""
a=input()
print(len(a))
"""

# Задание 2
"""
a,b=(str(i) for i in input().split())
print(b,a)
"""
# Задание 3

"""
a,b=input('Введите слово: '),input('Введите искомую букву: ')
scet=(-1)
index=0
if a.find('f')==-1:
    print('-1')
else:
    for i in a:                 
        if i==b:
            print(index,end=' ')
            break
        else:
            index+=1
    index=0
    for i in a:
        if i==b:
            scet=index
            index+=1
        else:
            index+=1
    print(scet)
"""

# Задание 4

"""
a= input()
print(a.replace('1','one'))
"""

# Задание 5

"""
a=input()
print(a.replace('@',""))
"""


