# OOPS BASICS
# Task 1: Define a class Student with attributes name and roll_number. Create an object of this class and print its attributes.
# class student():
#     name="Fareesa Hibah"
#     rollno=12

# x=student()
# print(x.name)
# print(x.rollno)


# Task 2: Define a class Rectangle with attributes length and width. Add a method area to calculate the area of the rectangle. Create an object and call the method.
# class rectangle():

#     def area(self,a,b):
#         return a*b
    
# arearect=rectangle()
# print(arearect.area(10,6))
# 
# class rectangle():

#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
        
#     def area(self):
#         return self.length*self.width

# rect=rectangle(10,6)
# print(rect.area())


#Task 3: Define a class Circle with a method circumference to calculate the circumference and another method area to calculate the area. Use π = 3.14.
# class circle:
#     def __init__(self,radius):
#         self.radius=radius

#     def circumference(self):
#         return 2*3.14*self.radius
    
#     def area(self):
#         return 3.14*(self.radius**2)

# x=circle(5)
# print(f"Circumference is: {x.circumference()}")
# print(f"Area is: {x.area()}")


# Task 4: Define a class Employee with a class attribute company_name and instance attributes name and salary. Print both class and instance attributes.
# class Employee:
#     company_name="Microsoft"
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

# x=Employee("Fareesa",10000)
# print(f"Nmae of the company: {x.company_name}")
# print(f"Name of the employee: {x.name}")
# print(f"Salary of the employee: {x.salary}")

# Task 5: Create a base class Animal with a method sound. Create a derived class Dog that overrides the sound method. Call the method from an object of Dog.
# class Animal:
#     def sound(self):
#         return "Sound"
# class Dog(Animal):
#     print("Bark")

# d=Dog()
# d.sound()

# Task 6: Create a class Book with attributes title and author. Add a method is_same_author that compares the authors of two book objects.
# class book:
#     def __init__(self,title,author):
#         self.title=title 
#         self.author=author
#     def is_same_author(self,other_book):
#         return self.author==other_book.author

# x=book("Wings of Fire","APJ Abdul Kalam")
# y=book("Ignited Minds","APJ Abdul Kalam")

# print(x.is_same_author(y))

####################################################################################################################################################

# ENCAPSULATION

# Write a Python class with a public attribute name and a public method greet() that prints "Hello, [name]". Access both the attribute and method from outside the class.
# class xyz():
#     def __init__(self):
#         self.name="Fareesa"
#
#     def greet(self):
#         print(f"Hello,{self.name}")
#
# x=xyz()
# print(x.name)
# x.greet()

# Create a class with a protected attribute _age and a method _show_age() that prints the value of _age. Access these members directly from an object and observe the output.
# class abc():
#     def __init__(self):
#         self._age=19
#   
#     def show_age(self):
#         print(f"AGE:{self._age}")
#
# class qwe(abc):
#     def show(self):
#         print()
#
# x=qwe()
# x.show_age()
# print(x._age)

# Create a class with a private method __secret(). Add a public method to call the private method, and demonstrate that the private method cannot be called directly from outside the class.
# class qrs():
#     def __init__(self):
#         self.__pin="1234"
    
#     def secret(self):
#         print(f"PIN:{self.__pin}")
    
# x=qrs()
# x.secret()
# print(x.__pin)  ### gives error


# Task 1 : Create a Book class to manage book information in a library. The class should have private attributes for the book title, author, and price. Implement getter and setter methods for each attribute and a function to create a Book instance with user input.
# class library():
#     def __init__(self,title,author,price):
#         self.__title=title
#         self.__author=author
#         self.__price=price

#     def set_title(self,title):
#         self.__title=title
    
#     def set_author(self,author):
#         self.__author=author
    
#     def set_price(self,price):
#         if price>0:
#             self.__price=price
#         else:
#             print("Enter correct amount.")

#     def get_title(self):
#         return self.__title
    
#     def get_author(self):
#         return self.__author

#     def get_price(self):
#         return self.__price

#     def view(self):
#         print(f"""Book title : {self.__title}
# Author is : {self.__author}
# Price of the book : {self.__price}""")
    
# def book():
#     title=input("Enter the title : ")
#     author=input("Enter the author name : ")
#     while True:
#         price=int(input("Enter the price of the book : "))
#         if price>0:
#             break
#         else:
#             print("Price must be more than 0.")
#     return library(title,author,price)

# x = book()
# x.view()

# Task 2 : Create an Employee class to manage employee information. The class should have private attributes for the employee name, position, and salary. Implement getter and setter methods for each attribute and a function to create an Employee instance with user input.
# class Employee_info():
#     def __init__(self,name,position,salary):
#         self.__name=name
#         self.__position=position
#         self.__salary=salary

#     def set_name(self,name):
#         self.__name=name
    
#     def set_position(self,position):
#         self.__position=position

#     def set_salary(self,salary):
#         if salary>0:
#             self.__salary=salary
#         else:
#             print("Enter correct amount.")

#     def get_name(self):
#         return self.__name
    
#     def get_position(self):
#         return self.__position
    
#     def get_salary(self):
#         return self.__salary
    
#     def view(self):
#         print(f"""Employee name : {self.__name}
# Position : {self.__position}
# Salary : {self.__salary}""")
        
# def info():
#     name = input("Enter employee's name : ")
#     position = input("Enter their position : ")
#     while True:
#         salary = int(input("Enter their salary : "))
#         if salary>0:
#             break
#         else:
#             print("Enter correct amount.")
#     return Employee_info(name,position,salary)

# x = info()
# x.view()

###########################################################################################################################################################################

#ABSTRACTION
# Task 1 :- Create an abstract class Shape with an abstract method area().
# Implement two subclasses, Circle and Rectangle, that inherit from Shape and calculate the area based on their respective formulas.
# Write a program to calculate and print the area of a circle with radius 5 and a rectangle with width 4 and height 6.
# from abc import ABC , abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius

#     def area(self):
#         return 2*3.14*self.radius 

# class Rectangle(Shape):
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b

#     def area(self):
#         return self.l*self.b

# x = Circle(5)
# print(f"Area of circle : {x.area()}")
# y = Rectangle(6,4)
# print(f"Area of Rectangle : {y.area()}")           


# Task 2 :-Create an abstract class Employee with the following abstract methods:
# calculate_salary(): Calculate the employee's salary.
# get_details(): Print details of the employee.
# Implement two subclasses, FullTimeEmployee and PartTimeEmployee, with their own salary calculation logic.
# Write a program to demonstrate these classes.
# from abc import ABC , abstractmethod
# class Employee(ABC):
#     @abstractmethod
#     def cal_salary(self):
#         pass
#     @abstractmethod
#     def get_details(self):
#         pass

# class FullTimeEmployee(Employee):
#     def __init__(self,name,salary):
#         self.salary=salary
#         self.name=name

#     def cal_salary(self):
#         print("Salary of full-time employee : ",self.salary)

#     def get_details(self):
#         print(f"""Full-time mployee name : {self.name}
# Their salary : {self.salary}""")

# class PartTimeEmployee(Employee):
#     def __init__(self,name,h_rate,h_worked):
#         self.name=name
#         self.h_rate=h_rate
#         self.h_worked=h_worked

#     def cal_salary(self):
#         return self.h_rate*self.h_worked
    
#     def get_details(self):
#         print(f"""Part-time employee name : {self.name}
# Their salary : {self.cal_salary()}""")
        
# x = FullTimeEmployee("Fareesa Hibah",1200000)
# y = PartTimeEmployee("Ayesha Rida",8,10000)

# x.cal_salary()
# x.get_details()

# y.cal_salary()
# y.get_details()


# Task 3:-Create an abstract class Animal with abstract methods sound() and move().
# Implement subclasses Dog and Bird, where:
# Dog defines sound as "bark" and move as "walk."
# Bird defines sound as "chirp" and move as "fly."
# from abc import ABC , abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass

#     @abstractmethod
#     def move(self):
#         pass

# class Dog(Animal):
#     def __init__(self):
#         self.s=""

#     def sound(self):
#         print("Bark")
    
#     def move(self):
#         print("Walk")

# class Bird(Animal):
#     def __init__(self):
#         self.s=""

#     def sound(self):
#         print("Chirp")
    
#     def move(self):
#         print("Fly")

# x=Dog()
# y=Bird()

# x.sound()
# x.move()

# y.sound()
# y.move()

#ask 4:- Create an abstract class Appliance with methods turn_on() and turn_off().
# Implement a Fan and a Light class, where:
# Fan prints "Fan is turned on" and "Fan is turned off."
# Light prints "Light is turned on" and "Light is turned off."
# Write a program to turn on and turn off both a fan and a light
# from abc import ABC , abstractmethod

# class Appliance(ABC):

#     @abstractmethod
#     def turn_on(self):
#         pass

#     @abstractmethod
#     def turn_off(self):
#         pass

# class Fan(Appliance):
#     def __init__(self):
#         self.a=""

#     def turn_on(self):
#         print("Fan is turned on.")

#     def turn_off(self):
#         print("Fan is turned off.")

# class Light(Appliance):
#     def __init__(self):
#         self.a=""

#     def turn_on(self):
#         print("Light in turned on.")

#     def turn_off(self):
#         print("Light is turned off.")

# x = Fan()
# y = Light()

# x.turn_on()
# x.turn_off()

# y.turn_on()
# y.turn_off()