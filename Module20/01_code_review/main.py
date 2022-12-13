students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def student_interests(dict):
    lst_of_interests = []
    surnames = ''
    for key in dict:
        lst_of_interests += (dict[key]['interests'])
        surnames += dict[key]['surname']
    len_surnames = len(surnames)
    return lst_of_interests, len_surnames


pairs = []
for i_pair in students.items():
    pairs += [(i_pair[0], i_pair[1]['age'])]
print('Список пар "ID студента — возраст": {0}'.format(pairs))


interests_lst = student_interests(students)[0]
length = student_interests(students)[1]
print('Полный список интересов всех студентов: {0}'.format(interests_lst))
print('Общая длина всех фамилий студентов: {0} символов'.format(length))


