import copy
def find_key(site_structure, name_dict, new_value):
    if name_dict in site_structure:
        site_structure[name_dict] = new_value
        return site_structure
    for name, value in site_structure.items():
        if type(value) == dict:
            find_key(value, name_dict, new_value)


site = {
            'html': {
                'head': {
                    'title': 'Куплю/продам телефон недорого'
                },
                'body': {
                    'h2': 'У нас самая низкая цена на iPhone',
                    'div': 'Купить',
                    'p': 'продать'
                }
            }
        }

quantity = int(input('Сколько сайтов: '))

for i in range(quantity):
    product_name = input('Введите название продукта для нового сайта: ')
    meaning = {'title': f'Куплю/продам {product_name} недорого', 'h2': f'У нас самая низкая цена на {product_name}'}
    for name_key in meaning:
        find_key(site, name_key, meaning[name_key])
    print('Сайт для {0}:'.format(product_name))
    for key, value in site.items():
        print('site = {0} \n    "{1}": {0}'.format('{', key))
        if type(value) == dict:
            for key2, value2 in value.items():
                print('        "{0}": {1} '.format(key2, '{'))
                if type(value2) == dict:
                    for key3, value3 in value2.items():
                        print('            "{0}": "{1}"'.format(key3, value3))
                print('       },')
        print('    }', '\n}')





