#checking  if a year uploaded is a leap year or not :

print("Enter the Year to find if its a Leap year or not:   ")


def is_leap(year):
    leap = False
    
    
    if year % 400 == 0:
        leap = True
        
    elif year % 100 == 0:
        leap =False
        
    elif year % 4 == 0:
        leap = True
            
    return leap
year = int(input())
print(is_leap(year))
