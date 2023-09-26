# Задание 1
"""
a=[int(i) for i in input().split()]
for i in a:
    if i%2==0:
        a.remove(i)
print(*a)
"""

# Задание 2
"""
a=[int(i) for i in input().split()]
otv=[]
i=1
for i in range(len(a)):
    if a[i]>a[i-1]:
        otv.append(a[i])
print(*otv)
"""

# Задание 3

"""
a=[int(i) for i in input().split()]
i=1
for i in range(len(a)):
    if i%2!=0:
        a[i],a[i-1]=a[i-1],a[i]
print(*a)
"""

# Задание 4

"""
a=[int(i) for i in input().split()]
min,max=0,0
for i in range(len(a)-1):
    if a[min]>a[i+1]:
        min=i+1
if a[min]>a[-1]:
    min=i+1
print(min)
for i in range(len(a)-1):
    if a[max]<a[i+1]:
        max=i+1
if a[max]<a[-1]:
    max=i+1
print(max)
a[max],a[min]=a[min],a[max]
print(a)

"""

# Задание 5

"""
a,b=[i for i in input().split()],[i for i in input().split()]
score=0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            score+=1
print(score)
"""

# Задание 6

"""
a,b=[i for i in input().split()],[i for i in input().split()]
new=[]
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            new.append(a[i])
new.sort()
print(*new)
"""
# Задание 7
"""
a=[i for i in input().split()]
new=[]
for i in range(len(a)):
    if new.count(a[i])<1 :
        print('НЕТ')
        new.append(a[i])
    else:
        print('ДА')
"""

# Задание 8

"""
a='Abrakadabra'
print(a[2])
print(a[-1])
print(a[:5])
print(a[:9])
print(a[0::2])
print(a[1::2])
print(a[::-1])
print(a[-1::-2])
"""

# Задание 9

"""
a=input()
j=len(a)
new=[]
for i in range(j//2+j%2,len(a)):
    print(a[i], end='')
for i in range(j//2+j%2):
    print(a[i], end='')
"""

# Задание 10
"""
a=input()
new=''
score=0
for i in range(len(a)):
    if a[i] == 'h':
        score += 1
    elif 0 < score < a.count('h'):
        new += ''
    else:
        new += a[i]
print(new)
"""

# Задание 11

"""
a=input()
new,old,dlo='','',''
score=0
for i in range(len(a)):
    if a[i] == 'h':
        score += 1
    elif score > a.count('h'):
        break
    elif 0 < score:
        old += a[i]
    else:
        new += a[i]
dlo += old[::-1]
new += dlo
for i in range(i,len(a)):
    new+=a[i]
print(new)
"""

# Задание 12

"""
a=input()
new,old,old_old='','',''
score=0

for i in range(len(a)):
    if a[i] == 'h':
        score += 1
        old+=a[i]
    elif score == a.count('h'):
        break
    elif 0 < score :
        old += a[i]
    else:
        new += a[i]

for j in range(len(old)):
    if j==0 or j==len(old):
        old_old+='h'
        continue
    elif a[j]=='h':
        old_old += 'H'
    else:
        old_old+=old[j]

new+=old_old

for i in range(i,len(a)):
    new+=a[i]
print(new)
"""