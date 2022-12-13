def one_list(old_list: list, new_list: list = []) -> list:
    if type(old_list) == int:
        new_list += [old_list]
    elif type(old_list) == list:
        for value2 in old_list:
            one_list(value2, new_list=new_list)
    return new_list

nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]
unpacked_list = one_list(nice_list)
print(unpacked_list)


