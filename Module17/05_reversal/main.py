text = input('Введите строку: ')

reverse = [pos for pos, char in enumerate(text) if char == 'h']

start = reverse[0]
end = reverse[len(reverse) - 1] - 1

print('Развернутая последовательность между первым и последним h:', text[end:start:-1])
