num=float(input("Enter The first number: "))
num2=float(input("Enter The second number: "))
print("\nSelect the operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice=input("Enter the choice (1/2/3/4): ")
if choice=='1':
    result=num+num2
    print("The result of addition is: ",result)
elif choice=='2':
    result=num-num2
    print("The result of subtraction is: ",result)
elif choice=='3':
    result=num*num2
    print("The result of multiplication is: ",result)
elif choice=='4':
    if num2!=0:
        result=num/num2
        print("The result of division is: ",result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice! Please select a valid operation.")