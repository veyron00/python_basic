def qhofstadter(seq: list):
    """
    Генерирует последовательность Q Хофштадтера.
    Ограничена 30 элементами последовательности.
    :param seq: Начальная последовательность.
    :return: q
    """
    count = 0
    while count < 30:
        count += 1
        if seq[1] < 2:
            try:
                q = seq[-seq[-1]] + seq[-seq[-2]]
                seq.append(q)
                yield q
            except IndexError:
                raise StopIteration()
        else:
            raise StopIteration()


sequence = [1, 1]
qsequence = qhofstadter(sequence)
print('{0}, {1}'.format(sequence[0], sequence[1]), end=', ')
for i in qsequence:
    print(i, end=', ')
