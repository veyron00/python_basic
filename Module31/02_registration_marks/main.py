import re

car_numbers = 'А578ВЕ777, ОР233787, К901МН666, СТ46599, СНИ2929П777, 666АМР666'  # Список номеров

private_pattern = r'\b\w*[АВЕКМНОРСТУХ]\d{3}\w*[АВЕКМНОРСТУХ]{2,3}\d{2,3}'
print("\nЧастные регистрационные номера.")
private_reg_marks = re.findall(private_pattern, car_numbers)
taxi_pattern = r'\b\w*[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}'

print('Список номеров частных автомобилей: {}'.format(private_reg_marks))
print("\nРегистрационные номера такси.")
taxi_reg_marks = re.findall(taxi_pattern, car_numbers)
print('Список номеров такси: {}'.format(taxi_reg_marks))