import threading
from threading import Thread, Lock
import time
from random import randint


class Bank:
    LOCK_ = threading.Lock()
    BALANCE = 0

    def deposit(self):
        for i in range(100):
            a = randint(50, 500)
            self.BALANCE = self.BALANCE + a
            print(f'Пополнение: {a}. Текущий баланс: {self.BALANCE}')
            if self.BALANCE >= 500 and self.LOCK_.locked():
                self.LOCK_.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            a = randint(50, 500)
            print(f'Запрос на снятие: {a}')
            if a <= self.BALANCE:
                self.BALANCE = self.BALANCE - a
                print(f'Снятие: {a}. Текущий баланс: {self.BALANCE}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.LOCK_.acquire()


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.BALANCE}')
