class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# p1=Person("Keshav",78)
# p1.show_info()

# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id

#     def show_info(self):
#         super().show_info()
#         print(f"Student ID: {self.student_id}")

# s1=Student("Abhinay",56,101)
# s1.show_info()

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f"My name is {self.name}"

#     def __len__(self):
#         return len(self.name)

# p1=Person("Keshav")
# p2=Person("Anand Srinivas Vaka")

# print(p1.name)
# print(len(p1.name))

# print(len(p1))
# print(len(p2))

# print("My name is:",p1.name)

# print(str(p1))

# print(str(p2))

# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
    
#     def showVector(self):
#         print(f"{self.x}i + {self.y}j")
    
#     def addTwoVector(self,obj):
#         self.x=self.x+obj.x
#         self.y=self.y+obj.y


# l1=Point(4,6)
# l2=Point(2,9)

# l1.showVector()
# l2.showVector()

# l1.addTwoVector(l2)
# l3=l1+l2
# l3.showVector()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other): # Overloading +
        return Point(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
p1 = Point(12, 13)
p2 = Point(4, 9)

print(p1.__dir__())
# p3=p1.__add__(p2)

p3=p1+p2
print(str(p3))

# p3 = p1 + p2
# print(p3) # Output: (6, 8)