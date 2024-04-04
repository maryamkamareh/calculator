num1 = float(input("Enter first number: "))
user_input = input("Enter operation")
num2 = float(input("Enter second number: "))
if user_input == "+":
    result = num1 + num2
    print("Result: " + str(result))
elif user_input == "-":
    result = num1 - num2
    print("Result: " + str(result))
elif user_input == "*":
    result = num1 * num2
    print("Result: " + str(result))
elif user_input == "/":
    if num2 == 0:
        print("Error: Division by zero")
    else:
        result = num1 / num2
        print("Result: " + str(result))
else:
    print("Invalid input. Please try again.")