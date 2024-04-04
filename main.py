def calculator(num1,operator, num2):
    def add_numbers(num1, num2):
        return num1 + num2

    def multiply_numbers(num1, num2):
        return num1 * num2

    def subtract_numbers(num1, num2):
        return num1 - num2

    def divided_numbers(num1, num2):
        return num1 / num2

    if operator == '+':
        result = add_numbers(num1, num2)
    elif operator == '*':
        result = multiply_numbers(num1, num2)
    elif operator == '-':
        result = subtract_numbers(num1, num2)
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero")
        else:
            result = divided_numbers(num1, num2)
    else:
        print("Invalid operator!")
        exit()
    print(f"{num1} {operator} {num2} = {result}")

calculator(7, "+", 4)