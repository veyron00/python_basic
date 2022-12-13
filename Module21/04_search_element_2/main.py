def search_func(name, dictionary, depth = None, __depth_count = 1):
	result = None
	if depth and depth < __depth_count:
		return result
	if name in dictionary:
			return 'Значение ключа: {0}'.format(dictionary[name])
	else:
		for dict_name in dictionary.values():
			if isinstance(dict_name, dict):
				result = search_func(name, dict_name, depth, __depth_count + 1)
				if result:
					break
			else:
				result = None
	return result


site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}
name = input('Введите искомый ключ: ')
y_or_no = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if y_or_no == 'y':
	depth = int(input('Введите максимальную глубину: '))
	print(search_func(name, site, depth))
elif y_or_no == 'n':
	print(search_func(name, site))

