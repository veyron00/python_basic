import random

def distribution(data: list) -> list:
    processed_list = []
    start = 0
    for _ in range(len(data) // 2):
        processed_list += [tuple(data[start :start + 2])]
        start += 2
    print('Новый список: {0}'.format(processed_list))

source_list = [random.randint(0, 10) for _ in range(10)]
print('Оригинальный список: {0}'.format(source_list))
distribution(source_list)