print('Задача 8. Вклады')

# Вклад в банке составляет X рублей.
# Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.

# Определите, через сколько лет вклад составит не менее Y рублей.

# Напишите программу,
# которая по данным числам X, Y, P определяет,
# сколько лет пройдёт, прежде чем сумма достигнет значения Y.

deposit_amount = int(input('Введите размер вклада: '))
interest_rate = int(input('Введите размер % ставки: '))
desired_amount = int(input('Введите желаемую сумму: '))
years_counter = 0

while deposit_amount < desired_amount:
  deposit_amount = int(deposit_amount + (deposit_amount * interest_rate / 100))
  years_counter += 1
print(f'Для накопления {desired_amount} руб. понадобится {years_counter} лет.')
  
