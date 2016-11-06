class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Sum(self):
        return (self.x + self.y)

    def Mul(self):
        return (self.x * self.y)

class Scientific(Calculator):
    def power(self):
        return pow(self.x, self.y)

cal = Scientific(2, 3)

print("Your result is : {}".format(cal.power()))
