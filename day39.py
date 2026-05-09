# from functools import lru_cache
# import time

# @lru_cache(maxsize=None) # No limit on number of cached calls
# def square(n):
#     time.sleep(2)
#     print(f"Calculating square of {n}")
#     return n * n

# # square(5)

# print(square(5))
# print(square(6))
# print(square(5))

import re
# text = "My phone number is 123-456-7890 7676-7976-78"

# result = re.search(r'\d+', text)
# result = re.findall(r'\d+', text)
# print(result)
# print(result.group())

# text = "My email is test123@gmail.com"
# updated = re.sub(r'\w+@\w+\.\w+', 'hidden@email.com', text)
# print(updated)

# b1=re.match(r'World', 'Hello World') # Match at beginning
# print(b1)

# b1=re.search(r'World', 'Hello World') # Found anywhere
# print(b1.group())

# pattern = re.compile(r'\d+')

# print(pattern.findall("I have 2 apples and 10 bananas"))

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

# asyncio.run(main())

# import asyncio


# async def fetch_data(site):
#     print(f"Fetching from {site}")
#     await asyncio.sleep(3) # simulate network delay
#     print(f"Done fetching {site}")


# async def main():
#     sites = ['Google', 'YouTube', 'Facebook']
#     tasks = [fetch_data(site) for site in sites]
#     await asyncio.gather(*tasks)

# asyncio.run(main())

# import threading
import time

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

from multiprocessing import Process

def calculate_square(numbers):
    print("Squares:")
    for n in numbers:
        time.sleep(1)
        print(f"{n}^2 = {n*n}")
def calculate_cube(numbers):
    print("Cubes:")
    for n in numbers:
        time.sleep(1)
        print(f"{n}^3 = {n*n*n}")
if __name__ == "__main__":
    nums = [2, 3, 4, 5]
    # Create processes
    p1 = Process(target=calculate_square, args=(nums,))
    p2 = Process(target=calculate_cube, args=(nums,))
    # Start processes
    p1.start()
    p2.start()
    # Wait for processes to finish
    p1.join()
    p2.join()
    print("Done with multiprocessing!")