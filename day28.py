
class Animal:
    name="Default"
    age=12

    def details(self):
        print(f"Animal name is: {self.name} and age is: {self.age}")


# d1=Animal()
# d1.name="Sheru"
# d1.age=2

# d2=Animal()
# d2.name="Harish"
# d2.age=4

# print(d2.name)
# print(d2.age)
# d1.details()
# Animal.details(d1)

# d2.details()

def fact(num1):
    if num1==1 or num1==0:
        return 1
    return num1*fact(num1-1)


# 5*fact(4)
# 5*4*fact(3)
# 5*4*3*fact(2)
# 5*4*3*2*fact(1)
# 5*4*3*2*1

print(fact(5))