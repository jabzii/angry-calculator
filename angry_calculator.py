operator = input("Enter the operator (+, -, *, /, **): ")
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
if operator =='+':
    result = num1 + num2
    print(f"you are such a dump ASS KIDOOO.....")
elif operator =='-':
    result = num1 - num2
    print(f"go get a pen and paper find it yourself ....")
elif operator =='*':
    result = num1 * num2
    print(f"not in a mood to answer such a lame question")
elif operator =='/':
    if num2 != 0:
        result = num1 / num2
        print(f"I dont know I am a fool....")
    else:
        result = "Error! Division by zero is not possiple."
elif operator == '**':
    result = num1 ** num2
    print("Go find it yourself....")
else:
    print(f"Enter the correct operator you fool....")