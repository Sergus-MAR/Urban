class Vehicle():  #Класс любого транспорта 
    __COLOR_VARIANTS = ['Red', 'White', 'Grey', 'Green', 'Blue', 'Yellow','Black']
    def __init__(self, owner, model, color, engine_power):  #Иннициализация атрибутов
        if isinstance(owner, str):
            self.owner = owner #владелец транспорта. (владелец может меняться)
        if isinstance(model, str):
            self.__model = model    #модель (марка) транспорта. (мы не можем менять название модели)
        if isinstance(engine_power, int):
            self.__engine_power = engine_power #мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
        if isinstance(color, str):
            self.__color = color    #название цвета. (мы не можем менять цвет автомобиля своими руками)    
        
    def get_model(self):    #Метод вывода данных модели
        print(f"Модель: {self.__model}") 
    def get_horsepower(self):   #Метод вывода данных мощьности
        print(f"Мощность двигателя: {self.__engine_power}")
    def get_color(self):    #Метод вывода данных цвета
        print(f"Цвет:  {self.__color}")
        
    def print_info(self):   #Метод вывода полных данных о авто
        Vehicle.get_model(self)
        Vehicle.get_horsepower(self)
        Vehicle.get_color(self)
        print(f"Владелец: {self.owner}")
        
    def set_color(self, new_color): #Метод сравнения и изменения цвета
        if isinstance(new_color, str):
            resault = False
            for color_list in self.__COLOR_VARIANTS:
                if color_list.lower() == new_color.lower():
                    self.__color = new_color
                    resault = True
                else:
                    continue
            if resault != True:
                print(f"Нельзя сменить цвет на {new_color}")
class Sedan(Vehicle):    #Класс седанов (дочерний класс класса Vehicle)
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()  
