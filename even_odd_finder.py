#setting variables
num1even = 0
num1odd = 0 
#Asks the user for the number range
num1 = float(input("Enter the first number of the range!"))
num2 = float(input("Enter the last number of the range!"))

if (num2 < num1):
    print ("Invalid input!")




#main calculation
while True:
    num1 = num1 + 1
    if (num1 % 2) == 0:
        print(round(num1), "is even")
        num1even = num1even + num1
    else:
        print(round(num1), "is odd")
        num1odd = num1odd + num1

    if (num1==num2):
        break

print(num1even)    
print(num1odd)
                
