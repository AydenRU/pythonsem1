# Задание 1
def Work1():
    a = ['one', 'two', 'one', 'three', 'two']
    b={}
    for i in a:
        if i not in b.keys():
            b[i] = 0
        else:
            b[i] += 1
        print(b[i], end=' ')

# Задание 2
def Work2():
    a = int(input('Введите количество синонимов : '))
    print(a)
    b = [input('Введите  синонимы :').split() for i in range(a)]
    c = {}
    d = []
    for i in range(len(b)):
        for j in range(len(b[i])):
            if d == []:
                d = b[i][j]
            else:
                c[d] = b[i][j]
                c[b[i][j]] = d
        d= []
    print('Ответ : ', c[input()])


# Задание 3
def Work3():
    a = int(input())
    b = [input().split() for i in range(a)]
    c = {}
    for i in range(len(b)):
        b[i][1]=int(b[i][1])
        if b[i][0] not in c:
            c[b[i][0]] = b[i][1]
        else:
            c[b[i][0]] += b[i][1]
    for i in sorted(c.keys()):
        print(i,c[i])

# Задание 4

def Work4():
    a = int(input())
    b = [input().split() for i in range(a)]
    c = {}
    for i in range(len(b)):
        for j in range(len(b[i])):
            if b[i][j] in c:
                c[b[i][j]] +=1
            else:
                c[b[i][j]] = 1
    for i, j in sorted(c.items(), key = lambda para: (para[1], para[0]) ):
        print(i)
        break

# Задание 5
def Work5():
    a_score_file = int(input())
    b_file = [input().split() for i in range(a_score_file)]
    c = {'write': 'W', 'read': 'R', 'execute': 'X'}
    a_score_op = int(input())
    b_op = [input().split() for i in range(a_score_op)]
    for i in range(len(b_op)):
        if b_op[i][0] in c:
            b_op[i][0] = c[b_op[i][0]]
    for i in range(len(b_op)):
        for j in range(len(b_file)):
            if b_op[i][1] in b_file[j][0] and b_op[i][0] in b_file[j][1:]:
                print('OK')
                break
            elif j == len(b_file)-1:
                print('Denied')

# Задание 6
def Work6():
    a_score_file = int(input())
    b_file = [input().split() for i in range(a_score_file)]

    a_score_op = int(input())
    b_op = [input().split() for i in range(a_score_op)]
    c={}
    print(b_op)
    for i in range(len(b_file)):
        for j in range(1,len(b_file[i])):
            c[b_file[i][j]] = b_file[i][0]

    for i in range(len(b_op)):
        for j in range(len(b_op[i])):
            if b_op[i][j] in c:
                print(c[b_op[i][j]])

# Задание 7
def Work7():
    a = int(input())
    b = [input().split() for i in range(a)]
    c = {}
    for i in range(len(b)):
        for j in range(len(b[i])):
            if b[i][j] not in c:
                c[b[i][j]] = 1
            else:
                c[b[i][j]] += 1
    for i,j in sorted(c.items(), key= lambda par:(par[1]),reverse=True):
        print(i,j)




a = input('Введите номер работы :')
if a == 'Задание 1':
    Work1()
elif a == 'Задание 2':
    Work2()
elif a == 'Задание 3':
    Work3()
elif a == 'Задание 4':
    Work4()
elif a == 'Задание 5':
    Work5()
elif a == 'Задание 6':
    Work6()
elif a == 'Задание 7':
    Work7()
