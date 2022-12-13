import re


def check_number(nums: list) -> None:
    """
    Проверяет формат номера телефона на корректность.

    :param nums: Список номеров телефона.
    :return: None
    """
    pattern = r'\d*[89]{1}\d{9}\b'
    print('Проверка номеров:')
    for i_phone in nums:
        if re.fullmatch(pattern, i_phone):
            print('Номер {} всё в порядке.'.format(i_phone))
        else:
            print('Номер {} не подходит'.format(i_phone))


phone_nums = ['9999999999', '999999-999', '99999x9999', '81234567890', '8123456789', '7894561236']

check_number(phone_nums)
