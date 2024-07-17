# Part_1
def print_params (a = 1, b = 'строка', c = True):
    '''Проверка работы функции с различными параметрами'''
    print(a, b, c)

print_params(b = 25) # вывод в консоль: 1 25 True
print_params(c = [1,2,3]) # вывод в консоль: 1 строка [1, 2, 3]
print_params() # в данном случае выводит в консоль параметры указанные по умолчанию: 1 строка True
# независимо от типа данных если их указать в вызове функции, параметры присвоят тип указанных данных
# print_params(a = 10, 11, False) за исключением случая неправильного позиционирования именованых параметров

# Part_2
values_list = [12.33, 'Text', False]
values_dict = {'a': 110.5,
               'b': 63,
               'c': 'Front'}
print_params(*values_list) #происходит последовательная передача параметров в зависимости от положения данных в списке
                           # values_list[0] - a; values_list[1] - b, values_list[2] - c
print_params(**values_dict)#происходит именованная передача параметров в зависимости от положения данных в списке
                           # values_dict['a'] - a; values_dict['b'] - b, values_dict['c'] - c

# Part_3
values_list_2 = [True, 'Text']
print_params(*values_list_2) # В данном примере функция примет параметры 'а' и 'b', в то время как 'c' присвоится значение по умолчанию.