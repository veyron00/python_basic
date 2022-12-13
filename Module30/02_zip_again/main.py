from typing import List, Tuple

if __name__ == '__main__':
    letters: List[str] = ['a', 'b', 'c', 'd', 'e']
    numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    print('Объединяем два списка с помощью функции map(), наподобие тому как это делает функция zip()')
    zipped: List[Tuple[str, int]] = list(map(lambda x, y: (x, y), letters, numbers))
    print('Объединенный список zipped: {}'.format(zipped))