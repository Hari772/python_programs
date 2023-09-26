class A:
    def display(self):
        print("CLASS A")
class B(A):
    def display(self):
        print("class B")
        super().display()
class C(B):
    def display(self):
        print("Class C")
        super().display()
        
        
c1=C()
c1.display()

