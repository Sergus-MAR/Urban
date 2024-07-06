grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
avrg_grades = list(map(lambda x,y: x/y, (list(map(sum, grades))), (list(map(len, grades))) ))
sorted_students=sorted(list(students))
students_grades = {}
students_grades=dict(map(lambda i, j: (i, j), sorted_students, avrg_grades))
print(students_grades)