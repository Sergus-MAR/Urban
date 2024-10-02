import io
from pprint import pprint

def custom_write(file_name, string):
    '''Позиционирование в файле'''
    strings_position = {}
    file = open (file_name,'wt',encoding='utf-8')
    counter = 1
    for element in string:
        strings_position[(counter, file.tell())] = element
        file.write(element + '\n')
        counter += 1
    file.close()
    return strings_position

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)







