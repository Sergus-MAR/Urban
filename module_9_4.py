# Lambda
first = 'Мама мыла раму'
second = 'Рамена мало было'
resault = list(map(lambda i, j: i == j, first, second))
print(resault)

# Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, "w") as file:
            for data in data_set:
                file.write(f'{data}\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# __call__
from random import choice
class MysticBall:
    def __init__(self, *words):
        self.words = words
    def __call__(self):
        randomizing_word = choice(self.words)
        return randomizing_word


first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Возможно', 'Невероятно')
print(first_ball())
print(first_ball())
print(first_ball())
