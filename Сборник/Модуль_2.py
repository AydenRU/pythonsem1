# Задание 1
"""
a=int(input())
print(a%10,a//10)
"""

# Задание 2
"""
a=int(input())
print((a%10)*10+a//10)
"""

# Задание 3
"""
a=int(input())
print(a%100)
"""

# Задание 4
"""
a=int(input())
print((a%100)//10)
"""

# Задание 5
"""
a=int(input())
g,b=0,10
for i in range(3):
    g+=(a%b)
    a//=10
print(g)
"""
# Задане 6
"""
a=float(input())
print(int((a*10)%10))
"""

# Задание 7
"""
a=int(input())
if a%100>=0:
    a=(a//100)+1
else:
    a=a//100
print(a)
"""
# Задание 8
'''
a=int(input('Введите целое число в диапозоне от 1 до 365: '))
if 1<=a<=365 :
    print(a+3)
else:
    print('Вне диапазона значения N')
'''
# Задание 9
"""
a=int(input())
print((a//60),':', a%60)
"""

# Задание 10
"""
a,b,c=int(input()),int(input()),int(input())
if a%2!=0:
    a=a//2+1
elif a%2==0:
    a=a//2
if b%2!=0:
    b=b//2+1
elif b%2==0:
    b=b//2
if c%2!=0:
    c=c//2+1
elif c%2==0:
    c=c//2
print(a+b+c)
"""







