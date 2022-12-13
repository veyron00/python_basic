# Задача 3. Собачьи бега
#
# В собачьих бегах участвует N собак, у каждой из них есть определённое
# количество очков за сезон. На огромном табло выводятся очки каждой
# собаки. Однако при выводе был обнаружен баг: собаки с наибольшим и
# наименьшим количеством очков поменялись местами! Нужно это исправить.
#
# Дан список очков из N собак. Напишите программу, которая меняет
# местами наибольший и наименьший элементы в списке.

dogs_scores = [30, 50, 18, 69, 45, 53, 37, 72, 46, 57]
print(dogs_scores)
maximum = -1000

minimum = 1000
count = -1
for score in dogs_scores:
    count += 1
    if maximum < score:
        maximum = score
        ind_max_score = count

    if minimum >= score:
        minimum = score
        ind_min_score = count
dogs_scores[ind_max_score], dogs_scores[ind_min_score] = dogs_scores[ind_min_score], dogs_scores[ind_max_score]
print(dogs_scores)