import re
text = """ Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, 
nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. 
Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate 
"""

# TODO здесь писать код
pattern = r'\b\w{4}\b'
data = re.findall(pattern, text)
print("Все слова состоящие из 4-х букв из переменной text: {}".format(data))