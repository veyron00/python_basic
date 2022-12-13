def sort_list(original_list):
    for num1 in range(len(original_list)):
        for num2 in range(1, len(original_list) + 1):
            if original_list[num1] < original_list[num2 - 1]:
                original_list[num1], original_list[num2 - 1] = original_list[num2 - 1], original_list[num1]

    return original_list


class_list1 = list(range(160, 176 + 1, 2))
class_list2 = list(range(162, 180 + 1, 3))
class_list1.extend(class_list2)
print(f'Объединенный список учеников: {class_list1}')
print(f'Отсортированный список учеников: {sort_list(class_list1)}')



