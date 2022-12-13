def slicer(object: tuple, num: int) -> tuple:
    object_tuple = []
    start = False
    for indx, value in enumerate(object):
        if value == num:
            start = True
        if value in object_tuple and value == num:
            start = False
            object_tuple += [value]
            break
        if start:
            object_tuple += [value]
    object_tuple = tuple(object_tuple)
    return object_tuple


# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10)
# num = int(input('Введите любое целое число: '))
# print(slicer(numbers, num))

