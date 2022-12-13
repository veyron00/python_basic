def union_func(data: dict) -> list:
    data_list = []
    for i_key, i_value in data.items():
        data_list += [i_key + i_value]
    data_list = tuple(data_list)
    print(data_list)


players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

union_func(players)
