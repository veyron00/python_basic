def calc():    
  operator = input('Выберите операцию: ')
  if operator != '+' and operator != '-' and operator != '*' and operator != '/':
      print('Ошибка: такой операции не существует. Попробуйте ещё раз.')
      return calc()
  operand_count = int(input('Сколько операндов? '))
  result = 0
  example = ''
  for num in range(1, operand_count + 1):
      if operator == '+':
          number = float(input(f'Введите операнд {num}: ')) 
          result += number
      if operator == '-':
          number = float(input(f'Введите операнд {num}: '))
          if result == 0:
              result = number
          else:
              result -= number
      if operator == '*':
          number = float(input(f'Введите операнд {num}: '))
          if result == 0:
              result = number
          else:
              result *= number
      if operator == '/':
          number = float(input(f'Введите операнд {num}: '))
          if result == 0:
              result = number
          else:
              result /= number
      if num < operand_count:				
              example += str(number)
              example += operator
      else:
              example += str(number)
              example += '=' + str(result)
  print(example)

calc()