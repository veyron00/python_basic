def zip_func(object1, object2):
    union_tuple = ((object1[i], object2[i]) for i in range((len(object1) + len(object2)) // 2))
    return union_tuple

iterated_object1 = 'abcd' #input('Строка: ')
iterated_object2 = (10, 20, 30, 40, 35) #input('Кортеж чисел: ')

union_object = zip_func(iterated_object1, iterated_object2)

print('Строка: {0}'.format(iterated_object1))
print('Кортеж чисел: {0}'.format(iterated_object2))


print('Результат:')
print(union_object)
for value in union_object:
    print(value)
