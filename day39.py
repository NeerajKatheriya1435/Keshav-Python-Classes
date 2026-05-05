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