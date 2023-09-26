def dirthbay(a,b):
    otv_1 = (a / day_year) * 100
    if otv_1 > 100:
        print(100)
    else:
        print(otv_1)
    otv_2 = (b / day_year) * 100
    if otv_2 > 100:
        print(100)
    else:
        print(otv_2)

a = int(input('Введите количество студентов :'))
day_year = 28*12
quantity_1 = (a * (a-1))//2
quantity_2=a-1
# Задание 1
otv_1 = (quantity_1/day_year)*100
otv_2 = (a/day_year)*100

# Задание 2

dirthbay(quantity_1,quantity_2)

