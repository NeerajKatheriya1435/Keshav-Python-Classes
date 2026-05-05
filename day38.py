
# import argparse

# parser = argparse.ArgumentParser(description="Simple calculator utility")

# parser.add_argument("num1", type=float, help="First number")
# parser.add_argument("num2", type=float, help="Second number")
# parser.add_argument("--operation", "-o", choices=["add", "sub"],
# default="add", help="Operation to perform")

# args = parser.parse_args()

# if args.operation=="add":
#     print(args.num1+args.num2)
# else:
#     print(args.num1-args.num2)

# input1=input("Enter the your name: ")
# print(input1)

# input1=int(input("Enter the your name: "))
# print(input1)
# if(input1!=""):
#     print(input1)

# if((inp1:=input("Enter your number: "))!=""):
#     print(inp1)

# line = input("Enter text (blank to stop): ")
# while line != "quit":
#     print("Line:", line)
#     line = input("Enter text (blank to stop): ")

# while (line := input("Enter text (blank to stop): ")) != "quit":
#     print("Line:", line)


# def count_up_to(n):
#     i = 1
#     while i <= n:
#         yield i
#         i += 1

# gen = count_up_to(5)

# print(next(gen))
# print(next(gen))

# def addTwonum(num1,num2):
#     next(gen)
#     print(num1+num2)

# addTwonum(6,4)

# print(next(gen))

import shutil
import os

# shutil.copy("*.py", "backup.txt")
# shutil.copy2("abhinay.txt", "backup_with_meta.txt")

# shutil.move("backup.txt", "folder1/backup.txt")
# shutil.rmtree("folder1")

shutil.copy("Rohan", "Ram")