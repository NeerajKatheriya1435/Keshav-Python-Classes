
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

class Human:
    company="Tesla"
    def __init__(self,name,age):
        self.name=name
        self.age=age
        # self.company="Tesla"

    def details(self):
        print(f"My name is: {self.name}")
        print(f"My age is: {self.age}")
        print(f"My company is: {self.company}")
    
    # @staticmethod
    # def average(num1,num2):
    #     print("The sum is:",(num1+num2)/2)


h1=Human("Keshav",38)
h2=Human("Rohan",46)

# h1.details()
# Human.average(6,4)

# h1.company="Hero"
Human.company="Hero"

h1.details()
h2.details()
