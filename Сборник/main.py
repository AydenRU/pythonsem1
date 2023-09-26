# Задание 1
"""
a,b,c=(int(input())),(int(input())),(int(input()))
a+=b+c
print(a)
"""

# Задание 2
"""
a,b=(int(input())),(int(input()))
s=1/2*(a*b)
print(s)
"""

# Задание 3
"""
print('Привет,'+' '+ input()+'!')
"""

# Задание 4
"""
a=int(input())
print('Следующее число для числа ', a ,': ', a+1)
print('Предыдущее число для числа ', a ,': ', a-1)
"""

# Задание 5
"""
a,b=int(input()),int(input())
print('Яблок у студентов: ', b//a,', ','в корзине: ', b%a)
"""

# Задание 6
"""
a=int(input())
print(a//3600, a//60)
"""
#Задание 7
"""
h1,m1,s1,h2,m2,s2=int(input()),int(input()),\
                  int(input()),int(input()),\
                  int(input()),int(input())
s1+=h1*3600+m1*60
s2+=h2*3600+m2*60
if s1>s2:
    difference=s1-s2
    print(difference)
else:
    difference=s2-s1
    print(difference)
"""