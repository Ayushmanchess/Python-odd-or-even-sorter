
#setting variables
num1odd = 0
num1even = 0


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

    else:
        print(round(num1), "is odd")

    if (num1==num2):
        break
                
