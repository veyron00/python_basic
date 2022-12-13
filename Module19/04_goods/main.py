goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for i_goods in goods.keys():
    for i_store in store.keys():
        if goods[i_goods] == i_store:
            quantity_goods = []
            purchase_price = []
            for i in range(len(store[goods[i_goods]])):
                quantity_goods.append(store[goods[i_goods]][i]['quantity'])
                purchase_price.append(store[goods[i_goods]][i]['quantity'] * store[goods[i_goods]][i]['price'])
            print('{0} - {1} шт., стоимость {2} руб.'.format(i_goods,
                    sum(quantity_goods), sum(purchase_price)))


