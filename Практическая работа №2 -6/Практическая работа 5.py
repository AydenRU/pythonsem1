word = list()
with open('Информация_Рейсов', 'w', encoding='utf-8') as long:
    with open('user.txt', 'r', encoding='utf-8') as user:
        for i in user:
            if 'Рейс' in i:
                word += [i.strip(' \n').split()]
    for i in range(len(word)):
        print(word[i])
        long.write(f"{[word[i][6]]} : Поезд № {word[i][1]} {word[i][5]} {word[i][4]}\n")
