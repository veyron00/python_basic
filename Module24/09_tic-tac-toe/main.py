class Cell:
    '''Класс клетки'''
    def __init__(self, num, status=False, value='--'):
        self.num = num # номер клетки
        self.value = value # значение клетки, по умолчанию --, принимает либо х или о
        self.status = status # Статус клетки занята или свободна





class Board:
    #  Класс поля, который создаёт у себя экземпляры клетки
    winning_combinations = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)
    ]
    def __init__(self, x=3, y=3):
        self.x = x
        self.y = y
        self.board = [Cell(i_num) for i_num in range(1, (x*y)+1)]


    def print_board(self):
        '''Выводит пронумерованные ячейки игрового поля.

        Просто для информации как ходить.'''
        for y in range(1):
            count = 0
            print('|', end='')
            for x in self.board:
                count += 1
                if count % 3 != 0:
                    print(' {} '.format(x.num), end='')
                    print('|', end='')
                elif count == 9:
                    print(' {} |'.format(x.num), end='\n')
                else:
                    print(' {} |'.format(x.num), end='\n')
                    print('|', end='')
    def game_board(self):
        '''Выводит заполненные игроками ячейки поля.'''
        for y in range(1):
            count = 0
            print('|', end='')
            for x in self.board:
                count += 1
                if count % 3 != 0:
                    print(' {} '.format(x.value), end='')
                    print('|', end='')
                elif count == 9:
                    print(' {} |'.format(x.value), end='\n')
                else:
                    print(' {} |'.format(x.value), end='\n')
                    print('|', end='')


class Player:
    '''Класс Игрок'''
    def __init__(self, name, token):
        self.name = name
        self.token = token # Чем играет игрок х или о
        self.move_list = [] # Список номеров ячеек куда ходил игрок.

    def players_move(self, board):
        '''Ход игрока
        если статус ячейки свободен, значение ячейки принимает х, или о,
        и ход разрешается, возвращает True.
        Если статус ячейки занят выводится соответствующее сообщение,
        возвращает False.'''
        try:
            num_cell = int(input('Игрок {}, введите номер ячейки чтобы пойти: '.format(self.name)))
        except (ValueError, IndexError):
            print('Ожидалось целое число, но введено было что-то другое.')
            num_cell = int(input('Игрок {}, введите номер ячейки чтобы пойти: '.format(self.name)))
        try:
            if board.board[num_cell-1].status == False:
                board.board[num_cell - 1].value = self.token
                board.board[num_cell - 1].status = True
                self.move_list.append(board.board[num_cell - 1].num)
                return True
            else:
                print('Эта ячейка занята.')
                return False
        except (ValueError, IndexError):
            print('Ожидалось целое число от 1 до 9, но введено было что-то другое.')




    def checking_for_winner(self, board):
        '''Проверяет есть ли победитель'''
        for i_comb in board.winning_combinations:
            count_num = 0
            for i_num in i_comb:
                if i_num in self.move_list:
                    count_num += 1
                if count_num == 3:
                    return 'Поздравляем победил игрок {}'.format(self.name)



board1 = Board()
board1.print_board()
player1 = Player('Alex', 'x')
player2 = Player('Jim', '0')
empty_cells = 9
while empty_cells > 0:


    if player1.players_move(board1):# Если True
        empty_cells -= 1 # уменьшает значение пустых ячеек
        board1.game_board()
    else:
        player1.players_move(board1)
        board1.game_board()

    if empty_cells == 0:
        print('Победила дружба!')
        break

    if player1.checking_for_winner(board1):
        print(player1.checking_for_winner(board1))
        break

    if player2.players_move(board1):
        empty_cells -= 1
        board1.game_board()
    else:
        player2.players_move(board1)
        board1.game_board()

    if empty_cells == 0:
        print('Победила дружба!')
        break

    if player2.checking_for_winner(board1):
        print(player2.checking_for_winner(board1))
        break


