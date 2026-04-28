userQuit = False
a = 0
b = 0
def menu():
    print("-------input your choice---------")
    print("1: plus\n2: minus\n3: multiply\n4: divide\n5: quit")
    Choice = int(input("input your choice: "))
    return Choice

def plus():
    a = int(input("input number one: "))
    b = int(input("input number two: "))
    return(a+b)
def minus():
    a = int(input("input number one: "))
    b = int(input("input number two: "))
    return (a - b)
def multiply():
    a = int(input("input number one: "))
    b = int(input("input number two: "))
    return (a * b)
def divide():
    a = int(input("input number one: "))
    b = int(input("input number two: "))
    if a == 0 :
        print("you cannot divide to zero enter num 1 again")
        a = int(input("input number one: "))
    elif b == 0 :
        print("you cannot divide to zero enter num 2 again")
        b = int(input("input number two: "))

    return (a / b)

while userQuit != True:
    userChoice = menu()
    if userChoice == 1:
        print("------plus------")
        print(plus())
        userChoice = 0

    if userChoice == 2:
        print("------minus------")
        print(minus())
        userChoice = 0

    if userChoice == 3:
        print("------multiply------")
        print(multiply())
        userChoice = 0

    if userChoice == 4:
        print("------divide------")
        print(divide())
        userChoice = 0

    if userChoice == 5:
        print("------quit------")
        quit()
