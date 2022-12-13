def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            return False
    else:
        return True


def crypto_processing(object):
    new_list = []
    for index, value in enumerate(object):
        if is_prime(index):
            new_list += [object[index]]
    return new_list

def crypto(func):
    return func



iterable_obj = 'О Дивный Новый мир!'
print(crypto(crypto_processing(iterable_obj)))
