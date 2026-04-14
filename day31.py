
def wrapper(func1):
    print("Hello Hii........")
    func1()
    print("Bye Bye.........")


def greet():
    print("Good Morning")

# greet()
# wrapper(greet)

def wrapper(func1):
    def newFunc():
        print("................")
        func1()
        print("................")
    return newFunc


@wrapper
def greet():
    print("Happy Birthday")

# @wrapper
def addTwoNum():
    a=7
    b=8
    print(a+b)

@wrapper
def multiNum():
    a=7
    b=4
    print(a*b)

greet()
addTwoNum()
multiNum()



