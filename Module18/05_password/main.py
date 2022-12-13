while True:
    password = input('Придумайте пароль: ')
    pass_len = len(password)
    pass_low = sum(map(str.islower, password))
    pass_up = sum(map(str.isupper, password))
    pass_dig = sum(map(str.isdigit, password))

    if (pass_len < 8) or (pass_up < 1) or (pass_dig < 3):
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break