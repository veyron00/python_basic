def output_number(num, start = 1):
    print(start)
    if num > start:
        output_number(num, start +1)



number = int(input('Введите num: '))

output_number(number)
