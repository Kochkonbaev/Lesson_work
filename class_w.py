'''Создайте класс хранящий названия групп студентов'''
class PyGroup:

    '''Счетчик групп'''

    amount = 0

    def __init__(self, name, *students):
        self.students = list(students)
        self.name = name
        # print(f'В группе {self.name} учаться {self.students} ')

        PyGroup.amount += 1

    '''Метод удаления студента'''

    def __del__(self):
        print(f'Удалена {self.name} грруппа!')

        PyGroup.amount -= 1

    '''Создайте метод добавления ученика'''

    def add(self, student):
        self.students.append(student)
        
    '''Метод для просмотра учеников и названия группы'''

    def Who(self):
        print(f'У нас в группе {self.name} учаться {self.students}')

    def howMany():
        print(f'У нас {PyGroup.amount} групп.')

    howMany = staticmethod(howMany)

group_math = PyGroup('5 class', 'Sasuke', 'Alex', 'Meerim', 'Dason')
group_math.Who()

group_lit = PyGroup('1 class', 'Bermet', 'Alina', 'Jako', 'Jay D')
group_lit.Who()

group_math.add('German')
group_math.Who()

PyGroup.howMany()

del group_math

PyGroup.howMany()
