first = ['Strings', 'Student', 'Computers', 'Test', 'Test_first']
second = ['Строка', 'Урбан', 'Компьютер', 'Test', 'Test_second']

first_result = ((len(first_str) - len(second_str)) for (first_str, second_str) in zip(first, second)
                if len(first_str) != len(second_str))
second_result = (len(first[position]) == len(second[position]) for position in range(min(len(first), len(second))))

print(list(first_result))
print(list(second_result))