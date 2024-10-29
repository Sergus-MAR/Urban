def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for elements in numbers:
        try:
            result += elements
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчета суммы - {elements}') 
    return result, incorrect_data


def calculate_average(numbers):
    count = 0
    try:
        for elements in numbers:
            if isinstance(elements, int):
                count += 1
        return personal_sum(numbers)[0] / count
    except TypeError:
        print("В numbers записан некорректный тип данных")
        return None
    except ZeroDivisionError:
        return 0

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать