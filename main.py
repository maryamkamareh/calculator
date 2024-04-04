def calculator():
    while True:
        print("Options:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'quit' to end the program")

        choose_operation = input(": ")

        if choose_operation == "quit":
            break
        elif choose_operation == "add":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 + num2
            print("Result: " + str(result))
        elif choose_operation == "subtract":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 - num2
            print("Result: " + str(result))
        elif choose_operation == "multiply":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 * num2
            print("Result: " + str(result))
        elif choose_operation == "divide":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if num2 == 0:
                print("Error: Division by zero")
            else:
                result = num1 / num2
                print("Result: " + str(result))
        else:
            print("Invalid input. Please try again.")

calculator()