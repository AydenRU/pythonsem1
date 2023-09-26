# Задание 1

"""
a = int(input())
i=2
while a%i!=0:
    i+=1
print(i)
"""

# Задание 2

"""
a = int(input("Введите число: "))
n = 0
while 2 ** (n + 1) <= a:
    n += 1
print(n, 2 ** n)
"""

# Задание 3

"""
a,b = int(input()),int(input())
day=1
while a<b:
    a+= (a/100)*10
    day+=1
print(day)
"""

# Задание 4

"""
a = int(input())
score = 0
while a!=0:
    b=int(input())
    if b>a:
        score+=1
    a = b
print(score)
"""

# Задание 5

"""
a = int(input())
n=1
otv=[]
while not n**2 >= a:
    otv.append(n**2)
    n+=1
print(*otv)
"""

# Задание 6

"""
a,back, n,score= int(input()),0,1,1
while n!=a and n<a:
    gost,n=n,n+back
    back=gost
    score+=1
if n>a:
    print(-1)
else:
    print(score)
"""

# Задание 7

"""
score,back,n= int(input()),0,1
while score!=1:
    gost,n=n,n+back
    back=gost
    score-=1
print(n)
"""

# Задание 8

"""
a,score,=int(input()),1
score_spisok=[]
while a!=0:
    b=int(input())
    if b==a:
        score+=1
    elif b!=a:
        score_spisok.append(score)
        score=1
    a=b
a=0
for i in range(len(score_spisok)-1):
    if score_spisok[i] > a:
        a=score_spisok[i]
print(a)
"""
