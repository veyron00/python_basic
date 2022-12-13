print('Задача 5. Недоделка 2')

# Вы всё так же работаете в конторе по разработке игр
# и смотрите различные программы прошлого горе-программиста.
# В одной из игр для детей, связанной с мультяшной работой с числами,
# вам нужно было написать код по следующим условиям:
# программа получает на вход два числа.
#
# В первом числе должно быть не меньше трёх цифр,
# во втором числе — не меньше четырёх,
# иначе программа выдаёт ошибку.
# Если всё нормально, то в каждом числе первая и последняя цифра меняются местами,
# а затем выводится их сумма.
#
#
# И тут вы натыкаетесь на программу,
# которая была написана прошлым программистом и которая как раз решает такую задачу!
# Однако старший программист сказал вам немного переписать этот код,
# чтобы он не выглядел так ужасно.
# Да и вам самим становится, мягко говоря, не по себе от него.
#
# Разбейте приведённую ниже программу на функции.
# Повторений кода должно быть как можно меньше.
# Также сделайте,
# чтобы в основной части программы был только ввод чисел, затем изменённые числа и вывод их суммы.

def num1_count(num1):
    first_num_count = 0
    temp = num1

    while temp > 0:
        first_num_count += 1
        temp = temp // 10

    if first_num_count < 3:
        print("В первом числе меньше трёх цифр.")
        
    else:
        last_digit = num1 % 10
        first_digit = num1 // 10 ** (first_num_count - 1)
        between_digits = num1 % 10 ** (first_num_count - 1) // 10
        num1 = last_digit * 10 ** (first_num_count - 1) + between_digits * 10 + first_digit
        print('Изменённое первое число:', num1)
        return num1
        
def num2_count(num2):        
    second_num_count = 0
    number2 = num2
    if num2 <= 0:
        pass
    else:
        while number2 > 0:
            second_num_count += 1
            number2 = number2 // 10

        if second_num_count < 4:
            print("Во втором числе меньше четырёх цифр.")
            
        else:
            last_digit = num2 % 10
            first_digit = num2 // 10 ** (second_num_count - 1)
            between_digits = num2 % 10 ** (second_num_count - 1) // 10
            num2 = last_digit * 10 ** (second_num_count - 1) + between_digits * 10 + first_digit
            print('Изменённое второе число:', num2)
            return num2
        
        
first_n = int(input("Введите первое число: "))
num1 = num1_count(first_n)
if num1 == None:
  pass
else:
  second_n = int(input("Введите второе число: "))
  num2 = num2_count(second_n)
  if num2 != None:
    print('\nСумма чисел:', num1 + num2)
    
