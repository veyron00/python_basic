import collections


def can_be_poly(word: str) -> bool:
    """
    Проверяет можно ли из принимаемой строки получиться палиндром.
    :param word: Принимаемая строка.
    :return: bool
    """
    all_elem_count = collections.Counter(word).most_common()
    if len(all_elem_count) > 2:
        if all(list(map(lambda x: True if x[1] % 2 == 0 else False, all_elem_count[:-1]))):
            return True
        else:
            return False
    else:
        if sum([i_let_num[1] for i_let_num in all_elem_count]) >= 3:
            return True
        else:
            return False


if __name__ == '__main__':
    print(can_be_poly('abcba'))
    print(can_be_poly('abbbc'))
    print(can_be_poly('cbbbc'))
    print(can_be_poly('ddddddddeeee'))
    print(can_be_poly('cbbabc'))
    print(can_be_poly('lsjajkdgfbSJDuibSDLK'))
