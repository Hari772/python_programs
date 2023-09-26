class Employee:
    name="Hari"
    marks=88
    centre="VAKADU"
    def printobj(self):
        print(f"my name is {self.name}")
hari=Employee()# basic class object
print(hari.name)
print(hari.marks)
print(hari.centre)
hari.printobj()
