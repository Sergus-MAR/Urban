import time
import random
import threading
from threading import Lock


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        dep_transaction = 100
        for i in range(1, dep_transaction):
            up_balance = random.randint(50, 500)
            if self.balance >= 500 and self.lock.locked(): #Проверка баланса и наличие блокировки
                self.lock.release() #Снимаем блокировку т.к. баланса достаточно для снятия от 50 до 500
            self.balance += up_balance
            print(f'Пополнение: {up_balance}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        take_transaction = 100
        for i in range(1, take_transaction):
            down_balance = random.randint(50, 500)
            print(f'Запрос на {down_balance}.')
            if down_balance <= self.balance:
                self.balance -= down_balance
                print(f'Снятие: {down_balance}. Баланс: {self.balance}.')
            else:
                print('Запрос отклонён, недостаточно средств.')
                self.lock.acquire() #Устанавливаем блокировку т.к. недостаточно средств
                time.sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
