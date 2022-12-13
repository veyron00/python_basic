import random
class Card:
    #  Карта, у которой есть значения
    #   - масть
    #   - ранг/принадлежность 2, 3, 4, 5, 6, 7 и так далее
    rank_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suit_list = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
    card_points = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

class Deck:
    '''Класс колода'''
    #  Колода создаёт у себя объекты карт
    dec_card = list()
    def __init__(self):
        '''Создание колоды из 52 карт.'''
        for i_suit in Card.suit_list:
            for i_rank in Card.rank_list:
                card = Card(i_rank, i_suit)
                self.dec_card.append(card)

    def distribution_of_cards(self):
        '''Раздача карт.

        Чтобы карты не повторялись из созданной колоды удаляются карты
        которые находятся на руках игроков.'''
        card = random.choice(self.dec_card)
        self.dec_card.pop(self.dec_card.index(card))
        return card.rank, card.suit

class Player:
    #  Игрок, у которого есть имя и какие-то карты на руках
    def __init__(self, name, deck):
        self.name = name
        self.card = [deck.distribution_of_cards() for _ in range(2)]
        self.count = 0 # Счетчик очков игрока
        self.count_len_list = 0 # Хранит длину списка карт игрока

    def get_the_cards(self, deck, pieces=1):
        '''Метод добора карт.'''
        self.pieces = pieces
        self.card.append(deck.distribution_of_cards())

    def print_score_info(self):
        '''Вывод информации о набранных очках.'''
        print('Игрок {} набрал {} очков.'.format(self.name, self.count))



    def scoring_points(self):
        '''Считает количество очков на руках игрока.

        Если у игрока 2 карты на руках просто считаются очки карт
        Если у игрока больше двух карт, считается только не посчитанная карта
        Если количество карт неизменилось, но была вызвана ф-я scoring_points,
        то тогда ничего не проиходит и сумма очков не меняется. '''
        if len(self.card) <= 2:
            for i_score in self.card:
                self.count += Card.card_points[i_score[0]]
        elif len(self.card) == self.count_len_list:
            pass
        elif self.count < 21 and len(self.card) > self.count_len_list:
            self.count += Card.card_points[self.card[len(self.card) - 1][0]]
        elif self.count > 22:
            if 'A' in self.card[len(self.card)]:
                self.count -= 10
        self.count_len_list = len(self.card.copy())



deck1 = Deck()
dealer = Player('Дилер', deck1)
player = Player('Костя', deck1)

winner = None
while not winner: # Пока winner не будет равен чему-то цикл работает.
    print('Карты на руках у {0} {1}.'.format(player.name, player.card))
    player.scoring_points() # Подсчет очков игрока
    player.print_score_info() # Вывод информации по очкам игрока
    dealer.scoring_points() # Подсчет очков дилера
    if player.count < 21:
        query = input('Добрать еще карту? y/n '.lower())
        if query == 'y':
            player.get_the_cards(deck1) # Добор карты игроком
            print('Карты на руках у {0} {1}.'.format(player.name, player.card))
            player.scoring_points() # Подсчет очков игрока
            player.print_score_info() # Вывод информации по очкам игрока
        else:
            pass

    if dealer.count < 19: # Если у дилера 19 и больше, то карту он не добирает
        dealer.get_the_cards(deck1) # Если меньше 19, то добирает карту
        dealer.scoring_points() # Подсчет очков дилера

    query = input('Вскрыться? y/n '.lower())

    if query == 'y':
        player.print_score_info()
        print('Карты на руках у {0} {1}.'.format(player.name, player.card))
        dealer.print_score_info()
        print('Карты на руках у {0} {1}.'.format(dealer.name, dealer.card))
        if player.count > dealer.count and player.count <= 21:
            print('Игрок {0} выиграл!'.format(player.name))
            winner = player.name
        elif dealer.count > player.count and dealer.count <= 21:
            print('Игрок {0} выиграл!'.format(dealer.name))
            winner = dealer.name
        elif player.count == dealer.count and player.count < 21 and dealer.count < 21:
            draw = 'Ничья!'
            print('Ничья!')
            winner = draw
        elif player.count < 21 and dealer.count > 21:
            print('Игрок {0} выиграл!'.format(player.name))
            winner = player.name
        elif dealer.count < 21 and player.count > 21:
            print('Игрок {0} выиграл!'.format(dealer.name))
            winner = dealer.name
        elif player.count > 21 and dealer.count > 21:
            loss = 'Оба игрока проиграли!'
            print(loss)
            winner = loss
        elif player.count == 21:
            print('Игрок {0} выиграл!'.format(player.name))
            winner = player.name
    elif query == 'n':
        pass


