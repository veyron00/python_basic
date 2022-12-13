def compress(str_txt):
    str_len = len(str_txt)
    result = ''

    if str_len > 0:
        i = 0
        while i < str_len:
            counter = 0
            curr_char = str_txt[i:i + 1]
            while i < str_len and str_txt[i] == curr_char:
                i += 1
                counter += 1
            result += curr_char + str(counter)
    return result


text = input('Введите строку: ')

print(compress(text))