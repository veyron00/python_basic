def my_sum(*args, num_list = [], counter = 0):
    for elem in args:
        if type(elem) == int:
            num_list += [elem]
            return num_list
        elif type(elem) == list or tuple:
            for elem1 in elem:
                my_sum(elem1, num_list=num_list)
    counter = 0
    for num in num_list:
        counter += num
    num_list = []
    return counter

seq = [[1, 2, [3]], [1], 3]
seq1 = 1, 2, 3, 4, 5

print(my_sum(seq))



