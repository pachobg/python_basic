num1 = float(input("Enter first number: "))
op = input("enter operator: ")
num2 = float(input("Enter second number: "))
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 == 0:
        print("Second number must be not 0")
    else:
        print(num1 / num2)
else:
    print("Enter correct operator ")
