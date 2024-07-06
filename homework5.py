# Part_1
immutable_var = 1, 2, 3, 4, "text", [1, 2, 3], True # создание кортежа
immutable_var_list = [1, 2, 3, 4, "text", [1, 2, 3], True] # создание списка
print(type(immutable_var))
print(type(immutable_var_list))
print(immutable_var.__sizeof__())
print(immutable_var_list.__sizeof__())
immutable_var[5].append('text')
immutable_var_list[5].append('text')
immutable_var_list.append("text")
print(immutable_var)
print(immutable_var_list)
print(immutable_var.__sizeof__())
print(immutable_var_list.__sizeof__())
# Кортеж позволяет менять только элементы типа "список", элементы других типов невозможно изменить в кортеже,
# это обусловленно экономией ресурса при необходимости использовать фиксированные данные, к примеру константы
# В свою очередь список в теле кортежа дает возможность с минимальным расходом ресурса памяти хранить часто
# используемые переменные. В данном примере на кортеж выделено 80 байт в отличии от 96 байт при аналогичных данных 
# в типе список

#Part_2
mutable_list = [10, 20, 30, "new text", (4, 5, 'text', True)]
print(mutable_list)
mutable_list[0] = mutable_list[4]
mutable_list[1] = "change text"
mutable_list[2] = 30
mutable_list[3] = 20
mutable_list[4] = 10
mutable_list.append('Добавляем текст в конец списка')
print(mutable_list)
