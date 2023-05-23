#fibonacci series using iteration
n = int(input("Till where do you want to print the Fibonacci series?  "))
print(0)
print(1)
a = 0 
b = 1
i = 1
for i in range(n):
    c = a + b
    a = b
    b = c
    print (c)
     