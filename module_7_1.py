import os.path

class Product:
    def __init__(self,name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"
        pass

    pass
class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        file_data = ''
        if os.path.isfile(self.__file_name):
            file = open(self.__file_name, 'r')
            file_data = (file.read())
            file.close()
        return file_data
    def add(self,*products):
        file_list = str(self.get_products()).replace('\n','')
        for i in products:
            file_buffer = self.get_products()
            if str(i) in file_list:
                print (f'Продукт {i} уже есть в магазине')
            else:
                file = open(self.__file_name, 'w')
                file.write(file_buffer + str(i)+'\n')
                file.close()
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1,p2,p3)

print(s1.get_products())