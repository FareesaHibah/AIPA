class Species:
    def a(self):
        print("This is the main/base/parent class.")

class Humans(Species):
    def b(self):
        print("This is child/derived/class.")

x=Humans()

x.a()
x.b()

class Motor:
    def c(self):
        print("a is parent class.")

    def d(self):
        print("b is also parent class.")

class Aeroplane(Motor):
    def c(self):
        print("Aeroplane is child class.")

class Ship(Motor):
    def d(self):
        print("Ship is also child class.")

x = Aeroplane()
x.a()
x.b()
x.c()

y = Ship()
y.a()
y.b()
y.d()

class Math:
    def add(self,a,b):
        return a+b

class Sub(Math):
    def sub(self,a,b):
        return a-b
    
class Div(Math):
    def div(self,a,b):
        return a/b

class Mul(Math):
    def mul(self,a,b):
        return a*b 

a=int(input("Enter value of a : "))
b=int(input("Enter value of b : "))

x = Sub()
print("Addition = ", x.add(a,b))   
print("Subtraction = ", x.sub(a,b))

y = Mul()
print("Multiplication = ", x.mul(a,b))

z = Div()
print("Division = ", x.div(a,b))

class Library:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def disp(self):
        print(f"""Title : {self.title} , 
Author : {self.author} , 
Price : {self.price}""")
        
class Book(Library):
    def __init__(self, title, author, price,year):
        super().__init__(title, author, price)
        self.year=year

    def disp2(self):
        super().disp()  
        print("Year of publication : ",self.year)    ### USED TO CALL ALL THE ATTRIBUTES IN THE PARENT CLASS. ###

x = Book("Ignited Minds","APJ Abdul Kalam",500,2005)
x.disp2()



