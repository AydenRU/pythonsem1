file = input('Введите название файла : ')
text = open(file, 'r',)
s =list()
summa = int(text.readline())
print(summa)
for i in range(summa):
    s.append(text.readline().strip('\n'))
print(s)
text.close()


