def add_everything_up(a, b):
    try:
        return a + b
    except TypeError as value_type:
        return f"Неправельный тип данных {a} и {b} - ответ:", str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))