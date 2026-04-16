
# str1="12345"

# print(str1[-1])
# print(str1[::-1])
# print(str1[::-1])

# num=563687
# rev=0
# while(num>0):
#     lastDigit=num%10
#     rev=rev*10+lastDigit
#     num=num//10
# print(rev)

# class Human:
#     company="Tesla"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         # self.company="Tesla"

#     def details(self):
#         print(f"My name is: {self.name}")
#         print(f"My age is: {self.age}")
#         print(f"My company is: {self.company}")
    
#     @staticmethod
#     def average(num1,num2):
#         print("The sum is:",(num1+num2)/2)


# h1=Human("Keshav",38)
# h2=Human("Rohan",46)

# # h1.details()
# # Human.average(6,4)

# # h1.company="Hero"
# Human.company="Hero"

# h1.details()
# h2.details()

# class Human:
#     company="Tesla"
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary

#     # @classmethod
#     # def change_company(cls, new_name):
#     #     cls.company = new_name

#     @classmethod
#     def from_string(cls, data_str):
#         name, age,salary = data_str.split('-')
#         return cls(name, int(age),int(salary))

# str1="Neeraj-56-4000"
# str2="Neeraj-56-4000"

# h1=Human("Neeraj",67,8000)
# h2=Human("Rohan",89,5000)

# print(h1.company)
# Human.change_company("Hero")
# print(h1.company)
# print(h2.company)

# h1=Human.from_string(str1)
# print(h1.name)
# print(h1.age)
# print(h1.salary)

class Human:
    company="Tesla"
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    # @classmethod
    # def change_company(cls, new_name):
    #     cls.company = new_name

    @classmethod
    def from_string(cls, data_str):
        name, age,salary = data_str.split('-')
        return cls(name, int(age),int(salary))
    
# p1=Human("Rohan",78,2000)
# print(dir(p1))
# print(p1.__dict__)

# str1="Hello"
# help(str1.upper)
# help(str1.split)

import math
num1=1639

temp1=num1
temp2=num1

count=0

while(temp1>0):
    count+=1
    temp1//=10

newNum=0
while(temp2>0):
    lastDigit=temp2%10
    newNum+=math.pow(lastDigit,count)
    temp2//=10

if(newNum==num1):
    print("Number is ArmStrong")
else:
    print("Number is not ArmStrong")

