import re
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
user_in = input("input your operation")
user_input = re.split(r'\+|\-|\*|\/', user_in)
user_op = re.findall(r'[-+*/]', user_in)
calculater = cal(float(user_input[0]), float(user_input[1]), user_op[0])
if user_op[0] == "+":
    print(calculater.add())
elif user_op[0] == "*":
    print(calculater.mul())
elif user_op[0] == "-":
    print(calculater.sub())
elif user_op[0] == "/":
    print(calculater.div())