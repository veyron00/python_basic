print('Задача 3. Посчитай чужую зарплату...')

# Бухгалтер устала постоянно считать вручную среднегодовую зарплату сотрудников компании
# и, чтобы облегчить себе жизнь, обратилась к программисту.
 
# Напишите программу,
# которая принимает от пользователя зарплату сотрудника за каждый из 12 месяцев 
# и выводит на экран среднюю зарплату за год.
sum_salary = 0 # the amount of salary for the year
for month in range(1,13): #
  salary = int(input(f'Введите размер зарплаты за {month} месяц: '))
  sum_salary += salary
average_monthly_salary = int(sum_salary / 12) #calculate the average monthly salary
print(f'Всего за год заработали {sum_salary} руб.') #output of the result
print(f'Среднемесячная зарплата за 12 месяцев составила {average_monthly_salary} руб.')
  

