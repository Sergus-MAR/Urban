first = int(input("Введите первое целочисленное число: "))
second = int(input("Введите второе целочисленное число: "))
third = int(input("Введите третье целочисленное число: "))
if first != second and first != third and second != third:
    print('0')
elif first == second and first == third:
    print('3')
else:
    print('2') 