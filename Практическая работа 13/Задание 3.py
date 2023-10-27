class Cell():
    """Клетка, ее номер и начальный символ"""
    def __init__(self, num):
        self.num = num
        self.call = ' '

    def __str__(self):
        return self.call


class Board(Cell):
    """Класс доска наследующий класс Cell"""
    def __init__(self):
        self.cells = []                 #клетки символов
        for i in range(9):
            self.cells.append(Cell(i + 1))
    def p(self):
        print(len(self.cells))

    def display(self):
        """Отображение экрана игры"""
        for i in range(3):
            print('-------------')
            out = '| '
            for j in range(3):
                out += str(self.cells[i * 3 + j]) + ' | '
            print(out)
        print('-------------')

    def update(self, cell_num, symbol):
        '''Замена символа в поле клетки'''
        if self.cells[cell_num - 1].call == ' ':
            self.cells[cell_num - 1].call = symbol
            return True
        else:
            return False

    def is_game_over(self):
        '''проверка на совподение символов данных условиях'''
        for i in range(3):
            if self.cells[i * 3].call == self.cells[i * 3 + 1].call == self.cells[i * 3 + 2].call and self.cells[i * 3].call != ' ':
                return True
        for i in range(3):
            if self.cells[i].call == self.cells[i + 3].call == self.cells[i + 6].call and self.cells[i].call != ' ':
                return True
        if self.cells[0].call == self.cells[4].call == self.cells[8].call and self.cells[0].call != ' ':
            return True
        if self.cells[2].call == self.cells[4].call == self.cells[6].call and self.cells[2].call != ' ':
            return True
        for cell in self.cells:
            if cell.call == ' ':
                return False
        return True

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.score = 0
    def get_move(self):
        '''Выбор пустой клетки'''
        while True:
            cell_num = int(input(self.name + ', введите номер клетки: '))
            if cell_num < 1 or cell_num > 9:
                print('Введите правильный номер клетки.')
                return self.get_move()
            else:
                return cell_num

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.current_player = player1

    def play_turn(self):
        '''Сама игра'''
        print(self.current_player.name + ' ходит:\n')
        self.board.display()
        self.board.p()
        cell_num = self.current_player.get_move()  #номер выбора клетки
        while not self.board.update(cell_num, self.current_player.symbol):      #Проверка на наличие символа в клетке
            print('Данная клетка занята.')
            cell_num = self.current_player.get_move()

        if self.board.is_game_over():                   #проверка на окончание игры
            print(self.current_player.name + ' победил!\n')
            self.board.display()
            self.current_player.score += 1
            return True

        if self.current_player == self.player1:   #Смена игрока
            self.current_player = self.player2
        else:
            self.current_player = self.player1
        return False

    def play_game(self):
        """Начало игры"""
        self.board = Board()                     #Вызов класса Доска
        self.current_player = self.player1       #за кем первый ход
        while not self.board.is_game_over():     #пока нет функции self.board.is_game_over(), цикл продолжаеться
            if self.play_turn():                 #Основная игра
                break

        print('Score:')
        print(self.player1.name + ': ' + str(self.player1.score))
        print(self.player2.name + ': ' + str(self.player2.score))

while True:
    player1 = Player('Игрок 1', 'X')
    player2 = Player('Игрок 2', 'O')
    game = Game(player1, player2)
    game.play_game()

    again = input('Хотите ли продолжить игру(да/нет): ')
    if again.lower() != 'да':
        break