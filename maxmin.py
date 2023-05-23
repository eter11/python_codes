#finding the maximum and minimum


total=int(input("enter how numbers you are comparing:"))
n = []

for i in range(total):
    n.append(int(input("enter number: ")))

print(n,"\n")

max = -9999999999999999
min = 99999999999999

for i in range(total):
    if max<n[i]:
        max = n[i]

    if min>n[i]:
        min= n[i]
print(f"Maximum number is {max} minimum number is {min}")


