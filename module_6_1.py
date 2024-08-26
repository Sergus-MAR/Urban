class Animal(): #Обьявление родительского класса животных
    alive = True
    fed = False
    
    def __init__(self, name):   #Иннициализация атрибутов классов животных
        self.name = name
        
    def eat(self, food):    #метод eat - проверка на сьедобность/несьедобность растерия с последующей обработкой данных
        if food.edible != True: #Несьедобное растение
            print(f"{self.name} нестал есть {food.name}")
            self.alive = False
        else:   #Сьедобное растение
            print(f"{self.name} сьел {food.name}")
            self.fed =True
                  
class Plant():   #Обьявление родительского класса растений
    edible = False
    
    def __init__(self,  name):
        self.name = name
        
class Mammal(Animal):   #Обьявление дочернего класса животных
    pass
        
class Predator(Animal): #Обьявление дочернего класса животных
    pass
       
class Fruit(Plant): #Обьявление дочернего класса растений
    edible: bool = True
    
class Flower(Plant):    #Обьявление дочернего класса растений
    pass


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)