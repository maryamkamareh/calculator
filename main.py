class cal():
    def __init__(self,num1, num2, operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator
    def add (self):
        return self.num1 + self.num2
    def mul (self):
        return self.num1 * self.num2
    def sub (self):
        return self.num1 - self.num2
    def div (self):
        return self.num1 / self.num2
user_input = input("input operation")
calculater = cal(float(user_input[0]), float(user_input[2]), user_input[1])
if user_input[1] == "+":
    print(calculater.add())
elif user_input[1] == "*":
    print(calculater.mul())
elif user_input[1] == "-":
    print(calculater.sub())
elif user_input[1] == "/":
    print(calculater.div())