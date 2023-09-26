'''this is a using a SUPER() FUNCTION  USING  ACLASS'''


class A:
    def __init__(self):
        print("CLASS A")
class B(A):
    def __init__(self):
        print("class B")
        super().__init__()
class C(B):
    def __init__(self):
        print("Class C")
        super().__init__()
        
        
c1=C()

    
    