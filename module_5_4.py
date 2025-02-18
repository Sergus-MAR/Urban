﻿class House:
    houses_history = []
    def __new__(cls, name, number_of_floors):
        House.houses_history.append(name)
        return object.__new__(cls)
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        
    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")
        

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
h4 = House('ЖК Стройный', 50)
print(House.houses_history)
h5 = House('ЖК Небольшой', 5)
print(House.houses_history)

# Удаление объектов
del h2
del h3
del h5
del h4

print(House.houses_history)
