def zip_func(*args):
    all_list = [list(val) for val in args]
    min_len = min(all_list)
    new_list = [all_list[value][iteribl] for iteribl in range(len(min_len))
                for value in range(len(all_list))]
    split_list = [new_list[i:i + len(all_list)] for i in range(0, len(new_list), len(all_list))]
    tuple_list = [tuple(lst) for lst in split_list]
    return tuple_list

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
d = {1, 2, 3, 4, 5, 6}
b = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7}
c = (1, 2, 3, 4, 5, 6, 7, 8)


print(list(zip(a, b, c, d)))