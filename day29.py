

class Animal:

    name="Default"
    age=0

    def details(self):
        print(f"Dog name is: {self.name} and age is: {self.age}")

a1=Animal()
a1.name="Kittu"
a1.age=10
# print(a1.name)
# print(a1.age)
# a1.details()
Animal.details(a1)

print("-"*20)

a2=Animal()
a2.name="Tommy"
a2.age=12
# print(a2.name)
# print(a2.age)
# a2.details()
Animal.details(a2)

# a3=Animal()
a3=Animal()

# print(a3.name)
# print(a3.age)
