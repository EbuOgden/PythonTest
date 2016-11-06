class student:
    def __init__(self, name):
        self.name = name
        self.marks = []
        print("Hello {}, welcome to school".format(name))

    def pullMarks(self, mark):
        self.marks.append(mark)

    def avg(self):
        return sum(self.marks)/len(self.marks)

newStudent = student("Mike")

newStudent.pullMarks(5)
newStudent.pullMarks(10)
newStudent.pullMarks(3)
newStudent.pullMarks(1)
newStudent.pullMarks(1)

print("Your average is : {}".format(newStudent.avg()) )

print("Your average is : {avg}".format(avg=newStudent.avg()))
