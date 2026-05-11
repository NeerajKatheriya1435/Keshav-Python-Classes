# import time
# from functools import lru_cache

# @lru_cache(maxsize=None)
# def square(n):
#     time.sleep(4)
#     print(f"Calculating square of {n}")
#     return n * n

# print(square(3))
# print(square(9))
# print(square(3))


# import re

# text = "My phone number is 123-456-7890"

# result = re.search(r'\d{3}-\d{4}', text)

# print(result.group())

# text = "My numbers are 123 and 456 shivam 43567890"
# matches = re.findall(r'\d{3}', text)
# print(matches) # ['123', '456']

# text = "My email is test123@gmail.com"
# updated = re.sub(r'\w+@\w+\.\w+', 'hidden@email.com', text)
# print(updated)

# import time

# def task1():
#     time.sleep(2)
#     print("Task 1 done")

# def task2():
#     time.sleep(2)
#     print("Task 2 done")

# task1()
# task2()

# import asyncio

# async def task1():
#     await asyncio.sleep(2)
#     print("Task 1 done")

# async def task2():
#     await asyncio.sleep(2)
#     print("Task 2 done")

# async def main():
#     await asyncio.gather(task1(), task2())

# print("Hello Program")
# asyncio.run(main())

# import threading
# import time
# def display():
#     for i in range(5):
#         print(f"Thread running: {i}")
#         time.sleep(1)

# # Creating thread
# t = threading.Thread(target=display)
# # Starting thread
# t.start()

# # Main thread continues

# for i in range(5):
#     print(f"Main thread: {i}")
#     time.sleep(1)

# # Wait for thread to finish
# t.join()

# print("Program finished")


# from multiprocessing import Process
# import time

# def calculate_square(numbers):
#     print("Squares:")
#     for n in numbers:
#         time.sleep(1)
#         print(f"{n}^2 = {n*n}")

# def calculate_cube(numbers):
#     print("Cubes:")
#     for n in numbers:
#         time.sleep(1)
#         print(f"{n}^3 = {n*n*n}")

# if __name__ == "__main__":
#     nums = [2, 3, 4, 5]

#     # Create processes
#     p1 = Process(target=calculate_square, args=(nums,))
#     p2 = Process(target=calculate_cube, args=(nums,))

#     # Start processes
#     p1.start()
#     p2.start()

#     # Wait for processes to finish
#     p1.join()
#     p2.join()

#     print("Done with multiprocessing!")

# def add(a, b=8):
#     print(a + b)
# def add(*tup):
#     print(tup)
#     print(sum(tup))

# add(3,b=3)
# add(3)
# add(4,7,7,8,4)

# def info(**data):
#     print(data)

# info(name="Neeraj", age=23)

# try:
#     a = int(input("Enter number: "))
#     print(10 / a)
# except:
#     print("Error occurred!")

# age=int(input("Enter your age: "))

# if(age<18):
#     raise Exception("You are not eligible")

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def area(self):
#         return 10 * 5
    
#     def engine(self):
#         return 10 * 5000
    
# r = Rectangle()
# print(r.area())
# print(r.engine())

# sq=[i*i for i in range(12)]
# print(sq)

# d = {x: x*x for x in range(5)}
# print(d)

# s = {x*x for x in range(5)}
# print(s)

# even = [x for x in range(10) if x % 2 == 0]
# print(even)