class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.__color = self.__is_valid_color(color)
        self.addcolor = True
        self.__sides = self.set_sides(*sides)
        self.addsides = True
    def get_color(self):    #возвращает список RGB цветов.
        return self.__color

    def __is_valid_color(self, color):
        '''служебный, принимает параметры r, g, b, который проверяет корректность переданных
        значений перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые
        числа в диапазоне от 0 до 255 (включительно)'''
        temp_color_list = (1, 1, 1)
        def temp_test_color(color):
            temp_resault = False
            temp_color = []
            if len(color) == 3:
                for i in range(len(color)):
                    if (color[i] in range(-1, 256)) and isinstance(color[i], int):
                        temp_color.append(color[i])
                    else:
                        continue
                if len(temp_color) == 3:
                    temp_resault = True
                else:
                    temp_resault = False
            else:
                temp_resault = False
            return temp_resault

        if hasattr(self, 'addcolor'):
            if temp_test_color(color):
                return color
            else:
                return self.__color
        else:
            if temp_test_color(color):
                return color
            else:
                return temp_color_list

    def set_color(self, r, g, b):
        ''' принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
            предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.'''
        self.__color = self.__is_valid_color((r, g, b))
    def __is_valid_sides(self, *sides):
        '''Cлужебная, принимает неограниченное кол-во сторон, возвращает True если все стороны
        целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях'''
        sides_list = []
        for element in sides:
            sides_list.append(element)
        def pozitiv_sides_value(sides_list):
            '''Вложенная функция проверки на отрицательные числа и целочисленные значения'''
            sides_resault = True
            for i in sides_list:
                if i > 0 and isinstance(i, int):
                    sides_resault = sides_resault * True
                else:
                    sides_resault = sides_resault * False
            return sides_resault
        match self.sides_count:
            case 1:
                if len(sides_list) == 1 and pozitiv_sides_value(sides_list):
                    return True
                else:
                    return False
            case 3:
                if len(sides_list) == 3 and pozitiv_sides_value(sides_list):
                    return True
                else:
                    return False
            case 12:
                if ((len(sides_list) == 1) or (len(sides_list) == 12)) and pozitiv_sides_value(sides_list):
                    return True
                else:
                    return False
    def get_sides(self):
        return self.__sides
    def set_sides(self, *new_sides):
        '''Функция назначения атрибута сторон фигуры. Производит проверку на премет создания атрибута и исходя из результата
        присваивает требуемые значения. В случае, если стороны, в зависимости от типа фигур, не прошли валидацию - назначает значения по
        умолчанию для каждого вида фигур'''
        sides = []
        for i in new_sides:
            sides.append(i)
        if hasattr(self, 'addsides'):
            if self.__is_valid_sides(*new_sides):
                self.__sides = sides
        else:
            match self.sides_count:
                case 1:
                    if len(sides) == 1 and self.__is_valid_sides(*new_sides):
                        return sides
                    else:
                        return [1]
                case 3:
                    if len(sides) == 3 and self.__is_valid_sides(*new_sides):
                        return sides
                    else:
                        return [1, 1, 1]
                case 12:
                    if (len(sides) == 1) and self.__is_valid_sides(*new_sides):
                        return sides * 12
                    elif (len(sides) >= 2 and len(sides) <= 12) and (min(sides) == max(sides)):
                        return [i*min(sides) for i in [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
                    else:
                        return [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# Создание класса Круг
class Circle(Figure):
    sides_count = 1
    def len_circle(self):
        return self.get_sides()
# Создание класса Треугольник
class Triangle(Figure):
    sides_count = 3
    def get_squar(self):
        triangel_sides = self.get_sides()
        s = (triangel_sides[0] + triangel_sides[1] + triangel_sides[2]) / 2
        area = (s * (s - triangel_sides[0]) * (s - triangel_sides[1]) * (s - triangel_sides[2])) ** 0.5
        return area
# Создание класса Куб
class Cube(Figure):
    sides_count = 12
    def get_volume(self):
        cube_sides = self.get_sides()
        return cube_sides[0] * cube_sides[1] * cube_sides[2]
#Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangel1 = Triangle((10,10,10), 10, 10, 10)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
# Проверка периметра (круга), это и есть длина:
print(circle1.len_circle())
# Проверка объёма (куба):
print(cube1.get_volume())
# Проверка площади треугольника
print(triangel1.get_squar())