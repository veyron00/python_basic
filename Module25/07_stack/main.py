class Stack:
    """
    Класс Стек.
    Attributes:
        args: Элементы экземпляра класса.
    """

    def __init__(self, *args):
        self.args = args

    def __str__(self):
        """
        Метод строкового представления объекта класса.
        :return: ''{0}'.format(self.args)
        :rtype: str
        """
        return '{0}'.format(self.args)

    def adding(self, objects):
        """
        Добавляет элемент в объект класса
        :param objects: Добавляемый элемент
        :return: None
        """
        self.args = self.args + (objects,)

    def removal(self):
        """
        Удаляет последний добавленный элемент.
        :return: None
        """
        if len(self.args) > 0:
            self.args = self.args[:-1]


a = Stack()
a.adding(4)
print('Элементы экземпляра класса Stack - {0}'.format(a))
a.adding(5)
print('Элементы экземпляра класса Stack - {0}'.format(a))
a.adding(6)
print('Элементы экземпляра класса Stack - {0}'.format(a))
a.removal()
print('Элементы экземпляра класса Stack - {0}'.format(a))
a.removal()
print('Элементы экземпляра класса Stack - {0}'.format(a))
a.removal()
print('Элементы экземпляра класса Stack - {0}'.format(a))
a.removal()
print('Элементы экземпляра класса Stack - {0}'.format(a))


class TaskManager:
    """
    Класс Менеджер задач.
    """

    def __init__(self, *args):
        self.args = args

    def __str__(self):
        """
        Метод строкового представления класса.
        :return: '{0}'.\
            format(sorted(self.args, key=lambda args: args[1]))
        :rtype: str
        """
        for i in sorted(manager.args, key=lambda args: args[1]):
            print(str(i[1]), str(i[0]))
        return '{0}'. \
            format(sorted(self.args, key=lambda args: args[1]))

    def new_task(self, *args):
        """
        Добавляет новые задачи.
        :param args: Параметры новой задачи.
        :type: tuple(str, int)
        :return: None
        """
        if args not in self.args:
            self.args = self.args + (args,)
        else:
            print('Такая задача уже создана.')

    def task_completed(self):
        """Удаляет последнюю добавленную задачу."""
        if len(self.args) > 0:
            self.args = self.args[:-1]
        else:
            print('Список задач пуст.')


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
manager.__str__()
print('Одна задача выполнена')
manager.task_completed()
manager.__str__()
