# Задание 1
"""
a=int(input())
if a%=0:
    print('Четное')
else:
    print('нечетное')
"""

# Задание 2

"""
a,b=int(input()),int(input())
if a>b:
    print(a)
else:
    print(b)
"""

# Задание 3

"""
a=int(input())
if a > 0:
    print(1)
elif a < 0:
    print(-1)
else:
    print(0)
"""

# Задание 4
"""
a = int(input())
if 100<=a<=999:
    print('Да')
else:
    print('Нет')
"""

# Задание 5

"""
a,b=int(input())
if a>0 or b>0:
    print('Да')
else:
    print('Нет')
"""

# Задание 6

"""
a= int(input())
if a//100 < (a//10)%10 and (a//10)%10 < a%10:
    print('Да')
else:
    print('Нет')
"""

# Задание 7

"""
a=int(input())
if a//1000 == a%10 and (a//100)%10 == (a//10)%10:
    print('Да')
else:
    print('Нет')
"""

# Задание 8

"""
a=int(input('Напиши чиcло месяца и получишь количество в нем дней :'))
if a == 1 or  a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
    print(a,31)
elif a == 2:
    print(a,28)
else:
    print(a, 30)
"""

# Задание 9

"""
a,b,c = int(input()),int(input()),int(input())
score=0
if a == b and a == c:
    print(3)
elif a == b :
    print(2)
elif a == c:
    score+=2
elif c == b:
    score+=2
else:
    print(0)
"""

# Задание 10

"""
a,b = int(input()),int(input())
if (a%2==0 and b%2!=0) or (b%2==0 and a%2!=0):
    print('Белая')
else:
    print('Чёрная')
"""

# Задание 11

"""
a,b,c,d= int(input()),int(input()),int(input()),int(input())
if ((a%2==0 and b%2!=0) or (b%2==0 and a%2!=0)) and\
        ((c%2==0 and d%2!=0) or (d%2==0 and c%2!=0)):
    print('Да')
elif((a%2==0 and b%2==0) or (b%2!=0 and a%2!=0)) and\
        ((c%2==0 and d%2==0) or (d%2!=0 and c%2!=0)):
    print('Да')
else:
    print('Нет')
"""

# Задание 12

"""
a,b=int(input()),int(input())
if a == 1 or  a == 3 or a == 5 or a == 7 or a == 8 or a == 10 and b <= 30:
    print(b+1,'-',a,'-',2023)
elif a == 1 or  a == 3 or a == 5 or a == 7 or a == 8 or a == 10 and b > 30:
    print(1,'-',a+1,'-',2023)
elif a == 2 and b<=27:
    print(b+1,'-',a,'-',2023)
elif a == 2 and b>27:
    print(1,'-',a+1,'-',2023)
elif a == 4 or a == 6 or a == 9 or a == 11 and b <= 29:
    print(b + 1, '-', a, '-', 2023)
elif a == 4 or a == 6 or a == 9 or a == 11 and b > 29:
    print(1, '-', a + 1, '-', 2023)
elif a == 12 and b <= 30:
    print(b + 1, '-', a, '-', 2023)
elif a == 12 and b > 30:
    print(1, '-', 1, '-', 2024)
"""