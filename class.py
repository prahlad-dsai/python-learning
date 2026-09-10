class Student:
    def __init__(self,name,course):
        self.name = name
        self.course = course
    def introduce(self):
        print(" My name is ", self.name)
        print("I am doing ", self.course, "course here")

student1 = Student("Prahlad", "DSAI")

student1.introduce()

