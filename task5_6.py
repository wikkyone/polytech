import time
import random


def game():
    status = False
    i = 3
    while not status:
        first = random.randint(1, 100)
        second = random.randint(1, 100)
        right_answer = first + second
        print(f"Новый пример: {first} + {second}?")
        answer = int(input())
        if answer == right_answer:
            status = True
            print("Поздравляю! Ваш ответ правильный")
        else:
            print(f"Неверно! Штрафная пауза: {i} секунды")
            time.sleep(i)
            i += 1
