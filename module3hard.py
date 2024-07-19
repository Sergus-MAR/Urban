def count_int_str(data_massiv):
    '''Предварительное разделение массива данных'''
    element_sum = 0
    for i in data_massiv:
        if type(i) == str or type(i) == int:
            element_sum = element_sum + count_elements(i)
        else:
            element_sum = element_sum + open_structur(i)
    return element_sum        

def count_elements(element_open):
    '''Подсчет количества элементов строкового и числового типов'''
    if type(element_open) == int:  # Подсчет чисел
        return element_open
    elif type(element_open) == str:  # Подсчет строковых элементов
        return len(element_open)

def open_structur(element): 
    '''Раскрытие составных элементов типа списка, кортежа, множества, словаря. Рекурсивная функция '''
    element_resault = 0
    if type(element) == set:   # преобразование множества в список
        element = list(element)
    if type(element) == list or type(element) == tuple: # раскрытие элементов списков и кортежей 
        for k in element:
            if type(k) == str or type(k) == int:
                element_resault = element_resault + count_elements(k)
            else:
                element_resault = element_resault + open_structur(k)
        return element_resault       
    elif type(element) == dict: # раскрытие элементов словаря
        for j in element:
            if type(element.get(j)) == str or type(element.get(j)) == int:
                element_resault = element_resault + count_elements(j) + count_elements(element.get(j))
            else: open_structur(element.get(j))    
        return element_resault
    elif type(element) == str or type(element) == int:
        element_resault = count_elements(element)
        return element_resault

# Основное тело программы
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print('Сумма чисел и количество символов = ', count_int_str(data_structure))         
    