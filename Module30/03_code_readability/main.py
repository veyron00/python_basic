from typing import List

first_method: List[int] = list(filter(lambda x: all(x % y != 0 for y in range(2, x)), range(2, 1000)))
print('Однострочный вариант нахождения простых чисел в диапазоне: \n{}'.format(first_method))


def is_prime(num: int) -> List[int]:
    """
    Проверяет числа от 2 до num, является ли оно простым.
    Простые числа добавляет в список.
    :
    :return: prime_num(list)
    :arg: num(int): Число до которого будут, проверятся числа.
    """
    prime_num = []
    for x in range(2, num + 1):
        prime = True
        for i in range(2, (x // 2) + 1):
            if x % i == 0:
                prime = False
                break
        if prime:
            prime_num.append(x)
    return prime_num


if __name__ == '__main__':
    second_method = is_prime(1000)
    print('Многострочный вариант нахождения простых чисел в диапазоне: \n{}'.format(second_method))
