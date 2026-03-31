class Animal:

    # name="Default"
    # age=0
    def __init__(self,name,age):
        print("Hello constructor")
        self.name=name
        self.age=age

    def details(self):
        print(f"Dog name is: {self.name} and age is: {self.age}")

a1=Animal("Kittu",10)
a1.details()

a2=Animal("Tommy",34)
a2.details()

a3=Animal("Sheru",12)
a3.details()

# a=1
# b=12
# c=12

# if (a>=b and a>=c):
#     print(a,"is greater")
# elif(b>=a and b>=c):
#     print(b,"is greater")
# else:
#     print(c,"is greater")