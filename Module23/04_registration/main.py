import pathlib
from pathlib import Path
import logging

formatter = logging.Formatter('%(message)s')

def setup_logger(name, log_file, level=logging.INFO):
    """Чтобы настроить столько регистраторов, сколько вы хотите /
    To setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# первый файловый логер
logger = setup_logger('first_logger', 'registrations_good.log')
logger.info('Здесь указаны правильные данные.')

# второй файловый логер
super_logger = setup_logger('second_logger', 'registrations_bad.log')
super_logger.error('Здесь указаны данные с ошибками.')

def another_method():
   logger.info('Inside method')





def validation_func(data: list):
    pass
    fragmented_list = list()
    for i_elem in data:
        for elem in [i_elem.split(' ')]:
            fragmented_list += [elem]
    # count = 0
    for ind, value in enumerate(fragmented_list):
        if len(value) >= 3:

            try:
                if (fragmented_list[ind][0].isalpha()):

                    try:
                        if ('@' in fragmented_list[ind][1]) and ('.' in fragmented_list[ind][1]):

                            try:
                                if (int(fragmented_list[ind][2]) > 10 and int(fragmented_list[ind][2]) < 99):
                                    logger.info(fragmented_list[ind][0] + ' ' + fragmented_list[ind][1] + ' ' + fragmented_list[ind][2])
                                else:
                                    raise ValueError

                            except ValueError:
                                msg4 = 'Поле «Возраст» НЕ является числом от 10 до 99'
                                print(msg4)
                                super_logger.error(fragmented_list[ind][0] + ' ' + fragmented_list[ind][1] + ' ' +
                                             fragmented_list[ind][2] + ' ' + msg4)

                        else:
                            raise SyntaxError

                    except SyntaxError:
                        msg3 = 'Поле «Имейл» НЕ содержит @ и . (точку)'
                        print(msg3)
                        super_logger.error(fragmented_list[ind][0] + ' ' + fragmented_list[ind][1] + ' ' +
                                             fragmented_list[ind][2] + ' ' + msg3)

                else:
                    raise NameError
            except NameError:
                msg2 = 'Поле «Имя» содержит НЕ только буквы'
                print(msg2)
                super_logger.error(fragmented_list[ind][0] + ' ' + fragmented_list[ind][1] + ' ' +
                                             fragmented_list[ind][2] + ' ' + msg2)

        try:
            if value == ['empty00']:
                raise IndexError
        except IndexError:
            msg1 = 'НЕ присутствуют все три поля'
            print(msg1)


    print('Завершено.')



def from_file_to_list(file_dir) -> list:
    data_list = list()
    with open(file_dir, 'r', encoding='utf-8') as file:
        for i_line in file:
            if i_line == '\n':
                data_list += ['empty00']
                continue
            for line in i_line.split('\n'):
                if line != '':
                    data_list += [line]
                elif line == None:
                    data_list += [line]
    return data_list


read_file_name = 'registrations.txt'
file_dir = Path(Path.cwd(), read_file_name)
data = from_file_to_list(file_dir)
validation_func(data)



