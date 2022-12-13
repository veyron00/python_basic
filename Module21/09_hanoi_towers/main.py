def move(n, x, y):

    def suitable_rod(x,y):
        return ( {1,2,3} - {x} - {y} ).pop()

    if n:
        suitable_rod = suitable_rod(x,y)
        move( n-1, x, suitable_rod )
        print('Переложить диск {0} со стержня номер {1} на стержень номер {2}'.format(n,x,y))
        move( n-1, suitable_rod, y )

n = int(input('Введите количество дисков: '))
move(n,1,3)