def search_identical_numbers(num1, num2):

    for year in range(num1, num2 + 1):
        for i in range(10):
            if str(year).count(f'{i}') == 3:
                print(year)


first_year = int(input('Введите первый год: '))
second_year = int(input('Введите второй год: '))
search_identical_numbers(first_year, second_year)