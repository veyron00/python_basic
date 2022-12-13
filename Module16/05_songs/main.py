violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

songs_quantity = int(input('Сколько песен выбрать? '))
duration = 0
for i in range(songs_quantity):
    name_song = input(f'Название {i + 1}-й песни: ')
    for num in range(len(violator_songs)):
        if name_song == violator_songs[num][0]:
            duration += violator_songs[num][1]
print(f'Общее время звучания песен: {round(duration, 2)} минуты')



