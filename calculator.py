# a simple calculator :-)

cont = True
while cont:
    a=float(input('enter first number:'))
    b=float(input('enter second number:'))
    n=input("press\nA: for addition\nS: for Substraction\nD: for Divison\nM: for Multiplication")
    if n=='A' or n=='a':
        c= a + b
        print(f"the sum of {a} and {b} is :{c}")
        q = input("Should we continue? ")
        if q == "Y" or q == "y":
            cont = True
        else:
            cont = False
    elif n=='s' or n=='S':
        c= a - b
        print(f"the sum of {a} and {b} is :{c}")
        q = input("Should we continue? ")
        if q == "Y" or q == "y":
            cont = True
        else:
            cont = False
    elif n=='D' or n=='d':
        c= a / b
        print(f"the divison of {a} and {b} is :{c}")
        q = input("Should we continue? ")
        if q == "Y" or q == "y":
            cont = True
        else:
            cont = False
    if n=='M' or n=='m':
        c= a * b
        print(f"the product of {a} and {b} is :{c}")
        q = input("Should we continue? ")
        if q == "Y" or q == "y":
            cont = True
        else:
            cont = False
    break
