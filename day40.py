# def add(a, b):
#     print(a + b)


# add(5, 3)

# def student(name, age=78):
#     print(name, age)

# student("Rohan",67)

# student(age=21, name="Rahul")

# student("Rahul")

# def total(**num1):
    # print(num1)
    # print(sum(num1))
    # print(num1)

# total(5,3,6)
# total(5,3,6,8,4)

# total(name="Neeraj", age=23)

# def factorial(num):

#     if(num==1 or num==0):
#         return 1
#     return num*factorial(num-1)

# 5*4*3*2*1

# print(factorial(5))

# def A(num):
#     if(num==1):
#         return 1
#     return num*B(num-1)


# def B(num):
#     if(num==0 or num==1):
#         return 2
#     return num*A(num-2)

# print(B(4))

# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)

# print(fib(6)) # 8

# for i in range(6):
#     print(fib(i))

# list1=[1,2,3,43,45]
# print(list1)

# l1=[i*i for i in range(15)]
# print(l1)

# d = {x: x*x for x in range(5)}
# print(d)

# even = [x for x in range(10) if x % 2 == 0]
# print(even)



# try:
#     a=int(input("Enter the number 1: "))
#     b=int(input("Enter the number 1: "))
#     # a=int(a)
#     # b=int(b)
#     print(a/b)

# except ValueError:
#     print("Value Error Problem")

# except ZeroDivisionError as e:
#     print("Exception Occured:",e)

# finally:
#     print("Important")

# age = int(input("Enter age: "))

# if age < 18:
#     raise Exception("You are not eligible")
# else:
#     print("Eligible")

# class MyError(Exception):
#     pass

# try:
#     raise MyError("This is a custom error")
# except MyError as e:
#     print("This is my messgae")

# num = -4
# if num < 0:
#     raise MyError("Number cannot be negative")

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass


# class Rectangle(Shape):
#     def area(self):
#         return 10 * 5
    

# r = Rectangle()
# print(r.area())