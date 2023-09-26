#instance varaible and class variable
class A:
    a=10
    b=20
    def display(self):
        print(f"Class variables are {self.a} and {self.b}")
a1=A()
a2=A()
a2.a=30
a2.b=40
print(f"instance variables are {a2.a} and {a2.b}")
a1.display()
