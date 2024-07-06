my_dict = {'Ivan': 2020, 'Fedor': 2018, 'Kiril': 1999, 'Irina': 1990}
print('Словарь ', my_dict)
print('Данные из словаря - ',my_dict.get('Ivan'))
print('Отсутствующие данные - ', my_dict.get('Oleg', 'Не найден'))
new_name_first = 'Karina'
new_data_first = 1955
new_name_second = 'Karina'
new_data_second = 1955
my_dict.update({new_name_first : new_data_first,
                new_name_second : new_data_second})
print('Удаленное значение - ', my_dict.pop('Fedor'))
print('Измененный словарь - ',my_dict)
my_set = {1,2,3,1,2,'word','Word',False, (1,2,3,1,2,3)}
print('Множество ',my_set)
my_set.update(['Hello', 236])
my_set.remove('word')
print('Измененное множество', my_set)
