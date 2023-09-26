import random as ra

def finish():
    if a == istina:
        print('Поздравляю!! Вы победили')
    else:
        print('Не повезло')
        print('Правельна дверь № ', istina)

istina=ra.randrange(1,4)
a= int(input('Есть три двери. Введите номер двери :'))
b=input('Вы уверенны в своем выборе (Y/N) :')
if b == 'Y':
    finish()
elif b == 'N':
    a = int(input('Введите номер двери :'))
    finish()
else:
    print('Некоректный ответ')
