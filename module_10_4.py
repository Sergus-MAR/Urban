import threading
import random
import time
from queue import Queue

class Table:
    def __init__(self, number):
        if isinstance(number, int):
            self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        if isinstance(name, str):
            self.name = name

    def run(self):
        start_time = 3
        end_time = 10
        time.sleep(random.randint(start_time, end_time))

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        '''Принимает неограниченное кол-во гостей (объектов класса Guest). Если есть свободный стол, то садить гостя за 
        стол (назначает столу guest), запускает поток гостя и выводить на экран строку "<имя гостя> сел(-а) за стол 
        номер <номер стола>". Если свободных столов для посадки не осталось, то помещает гостя в очередь queue и 
        выводить сообщение "<имя гостя> в очереди".'''
        for guest in guests:
            free_table = self.free_table_in_cafe() # ищем свободный стол
            if free_table:
                free_table.guest = guest # привязываем гостя к свободному столу
                guest.start() # запускаем поток (садим гостя за стол)
                print(f'{guest.name} сел(-а) за стол номер {free_table.number}')
            else:
                self.queue.put(guest) # помещаем гостя в очередь
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        '''Метод имитирует процесс обслуживания гостей. Обслуживание происходит пока очередь не пустая (метод empty) или
         хотя бы один стол занят. Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил 
         работу - метод is_alive), то выводит строки "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и "Стол 
         номер <номер стола> свободен". Так же текущий стол освобождается (table.guest = None).Если очередь ещё не пуста
         (метод empty) и один из столов освободился (None), то текущему столу присваивается гость взятый из очереди 
         (queue.get()). Далее выводится строка "<имя гостя из очереди> вышел(-ла) из очереди и сел(-а) за стол номер 
         <номер стола>" Далее запускается поток этого гостя (start)'''
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            # Запускаем цикл до тех пор, пока не освободятся все столы, т.е. не завершатся все потоки
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    # ожидаем завершения потока и освобождаем стол
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None

                if not self.queue.empty() and table.guest is None:
                    # садим гостя за стол
                    next_guest = self.queue.get()
                    table.guest = next_guest
                    next_guest.start()
                    print(f'{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')

    def free_table_in_cafe(self):
        '''Функция для поиска свободного стола - возвращает свободный стол - если найден, если нет - возвращает None'''
        for table in self.tables:
            if table.guest is None:
                return table
        return None


tables = [Table(number) for number in range(1, 6)]


guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

guests = [Guest(name) for name in guests_names]

cafe = Cafe(*tables)

cafe.guest_arrival(*guests)

cafe.discuss_guests()