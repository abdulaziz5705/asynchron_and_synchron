#Asinxron dasturlash -  bir vaqtda bajarilishini boshqarish.
# Bu, ayniqsa, dastur faylni o 'qish/yozish yoki tarmoq so'rovlarini yuborish kabi tashqi resurslarni kutish
# uchun ko'p vaqt sarflaydigan kiritish-chiqarish bilan bog'liq vazifalar uchun foydalidir.

import asyncio
import time
from datetime import datetime


async def task1():
    await asyncio.sleep(3)
    print("Task 1 solve")
    print("End task1")


async def task2():
    await asyncio.sleep(1)
    print("Task 2 solve")
    print("End task2")


async def task3():
    await asyncio.sleep(5)
    print("Task 3 solve")
    print("End task3")


async def task4():
    await asyncio.sleep(4)
    print("Task 4 solve")
    print("End task4")


async def task5():
    await asyncio.sleep(5)
    print("Task 5 solve")
    print("End task5")


async def task6():
    await asyncio.sleep(1)
    print("Task 6 solve")
    print("End task6")


async def task7():
    await asyncio.sleep(6)
    print("Task 7 solve")
    print("End task7")


async def task8():
    await asyncio.sleep(2)
    print("Task 8 solve")
    print("End task8")


async def main():
    print(datetime.now())
    await asyncio.gather(task1(), task2(), task3(), task4(), task5(), task6(), task7(), task8())
    print(datetime.now())
if __name__ == "__main__":
    asyncio.run(main())