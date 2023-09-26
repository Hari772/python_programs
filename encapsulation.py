class student1:
    def __init__(self):
        self.__read()

    def __read(self):
        print("He is reading\n")
        print("He is studying\n")
class student2(student1):
    __name="HARIPRASAD DUVVUREU"
    __rollno="20KB1A0546"
    def details(self):
        print("name:",self.__name)
        print("rollno:",self.__rollno)
    def display(self):
        print("Above details are shown correctly")
s=student2()
s.details()
s.display()
