num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
print("1.Addition \n")
print("2.Subtraction \n")
print("3.Multiplication \n")
print("4.Division \n")
print("5.Modulo \n")
print("-----------------")
choice=int(input("Enter your choice(1-5):"))

if(choice==1):
    print("Result =",num1+num2)
elif(choice==2):
    print("Result =",num1-num2)
elif(choice==3):
    print("Result =",num1*num2)
elif(choice==4):
    print("Result =",num1/num2)
elif(choice==5):
    if(num2!=0):
        print("Result =",num1%num2)
    else:
        print("Error. Division by zero is not allowed")
else:
    print("Invalid choice.")