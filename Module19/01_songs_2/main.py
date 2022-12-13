violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

songs_quantity = int(input('Сколько песен выбрать? '))
duration_songs = 0
for i_song in range(1, songs_quantity + 1):
    name_song = input('Название {0}-й песни:  '.format(i_song))
    duration_songs += violator_songs.get(name_song, 0)
print('Общее время звучания песен: {0} минуты'.format(round(duration_songs, 2)))