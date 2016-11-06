class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __init__(self):
        self.a = 5
        self.b = 10

    def add(self):
        return (self.a + self.b)

    def neg(self):
        return (self.a - self.b)

cal = calculator()

print("Total is : {total}".format(total=cal.add()) )

print("Minus is : {minus}".format(minus=cal.neg()))

cal1 = calculator(100, 50)

print("Total is : {total}".format(total=cal1.add()) )

print("Minus is : {minus}".format(minus=cal1.neg()))
