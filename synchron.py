#synchron bu ma'lumotlarni ketma-ket tarzda o'qiydi masalan:
#Bitta reques kelsa bitta javob qaytaradi barcha savollarni birinchi o'qib olish imkoniyati yoq

import time
from datetime import datetime


def task1():
    time.sleep(2)
    print("Task 1")
    print("End task1")


def task2():
    time.sleep(3)
    print("Task 2")
    print("End task2")
    task4()


def task3():
    time.sleep(1)
    print("Task 3")
    print("End task3")


def task4():
    time.sleep(2)
    print("Task 4")
    print("End task4")


def task5():
    time.sleep(4)
    print("Task 5")
    print("End task5")


def task6():
    time.sleep(2)
    print("Task 6")
    print("End task6")


def task7():
    time.sleep(1)
    print("Task 7")
    print("End task7")


def task8():
    time.sleep(6)
    print("Task 8")
    print("End task8")


def task():
    print(datetime.now())
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    task7()
    task8()
    print(datetime.now())


if __name__ == "__main__":
    task()

