print('Задача 3. Апгрейд калькулятора')


# Степан, как и большая часть населения планеты,
# для расчёта суммы и разности чисел использует калькулятор.
#
# Однако в работе ему нужно
# делать не только  обычные действия вроде сложения и вычитания,
# а делать что-то вручную он уже устал.
#
# Поэтому Степан решил немного расширить функциональность своего калькулятора.
#
# Напишите программу,
# которая спрашивает у пользователя число и действие,
# которое нужно с ним сделать:
# вывести сумму его цифр,
# вывести максимальную цифру или вывести минимальную цифру.
#
# Каждое действие оформите в виде отдельной функции,
# а основную программу зациклите.
def sum_num(num):
    summ_number = 0
    while num > 0:
      count = num % 10
      summ_number += count
      
      num //= 10
    print('Сумма цифр равна', summ_number)
    


def max_num(num):
    largest_number = 0
    while num > 0:
      split_num = num % 10
      if split_num > largest_number:
        largest_number = split_num
      num //= 10
    print("Наибольшее число равно", largest_number)
    


def min_num(num):
    if num == 0:
      print("Наименьшее число равно", num)
    smaller_number = 10
    while num > 0:
      split_num = num % 10
      
      if split_num < smaller_number:
        smaller_number = split_num
      
      num //= 10
      
    print("Наименьшее число равно", smaller_number)
    


def calc():
    print('---Операции над числами---')
    num = int(input('Введите число: '))
    print(
        '1 - Вывести сумму цифр, 2 - Вывести максимальную цифру, 3 - Вывести минимальную цифру'
    )
    action = int(input('Введите 1, 2, или 3: '))
    if action == 1:
        sum_num(num)
        calc()
    elif action == 2:
        max_num(num)
        calc()
    elif action == 3:
        min_num(num)
        calc()


calc()
