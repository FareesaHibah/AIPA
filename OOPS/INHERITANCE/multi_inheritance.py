class A:
    def abc(self):
        print("Hello! This is class A.")

class B(A):
    def bcd(self):
        print("This is B ,subclass of A.")


class C(A):
    def cde(self):
        print("This is C, subclass of A.")

class D(A):
    def xyz(self):
        print("This is D. subclass of A.") 

class E(B,C,D):
    pass

x = E()
x.abc()
x.bcd()
x.cde()
x.xyz()


class NSTI:
    def __init__(self,lunch):
        self.lunch = lunch

class Lab:
    def __init__(self,lab):
        self.lab = lab

class AI(NSTI,Lab):
    def __init__(self, lunch,lab,computer):
        NSTI.__init__(self,lunch)
        Lab.__init__(self,lab)
        self.computer = computer

    def disp(self):
        print(f"Lunch : {self.lunch}, Lab : {self.lab}, Computer : {self.computer}")

lunch = input("Enter lunch menu : ")
lab = input("Which lab are you using? ")
computer = input("Which computer are you using? ")

x = AI(lunch,lab,computer)
x.disp()

