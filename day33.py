# class Human:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     def details(self):
#         print("Name is:",self.name)
#         print("Age is:",self.age)
    
#     @property
#     def get_name(self):
#         return "Mr. "+self.name
    
#     @get_name.setter
#     def set_name(self,value):
#         if len(value) > 2:
#             if(value.isdigit()):
#                 print("Value can not be in digit")
#             else:
#                 self.name = value

        
#         else:
#             print("Invalid name")



# h1=Human("Abhinay",25)
# h2=Human("Rohan",28)

# print(h1.name) # accessing the value
# h1.name="#$%^&*()" # update the property
# print(h1.name) # accessing the value

# h1.details()
# h2.details()

# h1.name="Rohan"

# h1.name="Rohan"
# print(h1.name)

# h1.set_name="Shivam"
# print(h1.get_name)
# print(h2.get_name)

# Human.details(h2)

# class Human:
    
#     def eat(self):
#         print("I can eat the food")

#     def walk(self):
#         print("I can walk")

# class Teacher(Human):
#     def teach(self):
#         print("I can teach")

# class Programmer(Teacher):

#     def program(self):
#         print("I can program")


# h1=Human()
# h1.eat()

# t1=Teacher()
# t1.eat()
# t1.teach()

# t1=Programmer()
# t1.eat()
# t1.teach()
# t1.program()

# class Mother:
#     def eat(self):
#         print("I can eat the food")

#     def walk(self):
#         print("I can walk")

# class Father:
#     def teach(self):
#         print("I can teach")

#     def kick(self):
#         print("I can Kick")

# class Son(Mother,Father):

#     def program(self):
#         print("I can program")
    


# s1=Son()
# s1.details()
# s1.eat()
# s1.teach()
# s1.program()


# class Mother:
#     def eat(self):
#         print("I can eat the food")

#     def walk(self):
#         print("I can walk")

# class Father:
#     def teach(self):
#         print("I can teach")

#     def kick(self):
#         print("I can Kick")

#     def car(self):
#         print("Honda")

# class Son(Father):

#     def program(self):
#         print("I can program")

#     def car(self):
#         super().car()
#         print("Rangerover")

# s1=Son()
# s1.car()


class Mother:
    def __init__(self,name):
        self.__gender=name # private
        # self._age=name #protected
        # self.name=name #public

    def eat(self):
        print("I can eat the food",self.__name)


m1=Mother("Geeta")

# m1.eat()
# print(m1.__name)
# m1.__name="Suman"
# print(m1.name)
# m1._Mother__name="Suman"
# print(m1._Mother__name)