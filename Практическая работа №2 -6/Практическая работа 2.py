import random as ra

def menu():
    print('Добро пожаловать в "Свою игру"\n', 'Хорошего время провождения! =3' )
    print('Пожалуйста выберете сложность игры.\n','Легко - 7 жизней\n','Нормально - 5 жизни\n','Сложно - 3 жизни\n')
    complexety = input('От вашего выбора будет зависеть количество попыток : ')
    live_word = {'Легко' : 7, 'Нормально' : 5, 'Сложно' : 3}
    live = live_word[complexety]
    return live_word, live, complexety

def agein(live_word, live, complexety,word,word_game,b):
    if b == 'Y' and live > 0:
        live = live_word[complexety]
        word.remove(word_game)
        my_game(live_word, live, complexety)
    elif b == 'Y' and live == 0:
        live = live_word[complexety]
        my_game(live_word, live, complexety)
    elif b == 'N':
        print('Пока)')
        exit(0)

def my_game(live_word, live, complexety):
    word = ['книга', 'месяц', 'ручка', 'шарик', 'олень', 'носок','компьютер','адвокат','обоятельный']
    word_game = ra.choice(word)
    print(word_game)
    stels_word_game = ['|' for i in range(len(word_game))]

    while live != -1:
        if '|' not in stels_word_game:
            print('Поздравляю с прохождением этапа!')
            b = input('Будете продолжать игру ? Y/N : ')
            agein(live_word, live, complexety,word,word_game,b)
        elif live == 0:
            b = input('Вы проиграли. Будете продолжать игру ? Y/N : ')
            agein(live_word, live, complexety,word,word_game,b)

        b = input()
        if b in word_game:
            for i in range(len(word_game)):
                if b == word_game[i]:
                    for j in range(len(word_game)):
                        if b == word_game[j]:
                            stels_word_game[j] = b
                    print(*stels_word_game)
                    break
                elif b == len(word_game) and b == word_game:
                    stels_word_game = b
                    print(*stels_word_game)
                    break
        elif live != 0:
            live -= 1
            print('Минус здоровье : ', live)

live_word, live, complexety = menu()
my_game(live_word, live, complexety)




