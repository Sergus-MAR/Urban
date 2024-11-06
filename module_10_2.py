import time
import threading


class Knight(threading.Thread):
    def __init__(self, name:str, power:int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def battle (self, name, power, enemies = 100):
        days = 0
        while enemies:
            time.sleep(1)
            days += 1
            enemies -= power
            print(f'{name}, сражается {days} день(дня)..., осталось {enemies} воинов')
        print(f'{name} одержал победу спустя {days} дней(дня)!')

    def run(self):
        print(f'{self.name}, на нас напали')
        self.battle(self.name, self.power)


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print(f'Все битвы закончились!')