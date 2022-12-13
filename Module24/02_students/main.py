class Student:
    def __init__(self,lst_name, first_name, group_number, academic_perfomans):
        self.lst_name = lst_name
        self.first_name = first_name
        self.group_number = group_number
        self.academic_perfomans = academic_perfomans

stud1 = Student('Смирнов', "Андрей", 1, [5, 7, 8, 9, 10])
stud2 = Student('Иванов', "Михаил", 2, [10, 5, 8, 8, 7])
stud3 = Student('Горбачев', "Александр", 2, [9, 4, 6, 6, 6])
stud4 = Student('Воронцова', "Галина", 9, [9, 10, 9, 9, 10])
stud5 = Student('Бережной', "Иван", 5, [6, 8, 7, 7, 5])
stud6 = Student('Баварцева', "Ольга", 1, [8, 8, 9, 7, 6])
stud7 = Student('Долгин', "Геннадий", 6, [7, 6, 9, 7, 6])
stud8 = Student('Алферова', "Анастасия", 5, [8, 8, 8, 7, 8])
stud9 = Student('Крючков', "Борис", 6, [5, 5, 6, 7, 9])
stud10 = Student('Дроздова', "Вероника", 9, [7, 8, 9, 7, 8])

student_list = [stud1, stud2, stud3, stud4, stud5, stud6, stud7, stud8, stud9, stud10]

new_list = sorted(student_list, key=lambda student: # Сортируем список с экземплярами класса Student по среднему баллу.
sum(student.academic_perfomans) / len(student.academic_perfomans))


print('|', 'Фамилия', '|', "Имя", '|', "Сумма баллов", '|', "Оценки", '|', "Ср. балл")
print(80 * '-')
for i in new_list:
    print(i.lst_name, i.first_name, sum(i.academic_perfomans),
          i.academic_perfomans, sum(i.academic_perfomans) / len(i.academic_perfomans))