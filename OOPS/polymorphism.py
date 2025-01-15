### CALLING METHODS OF SAME NAME THROUGH FUNCTION ###
# class A:
#     def x(self):
#         return "Hi"
    
# class B:
#     def x(self):
#         return "Fareesa"
    
# def z(s):
#     return s.x()

# r = A()
# a = B()

# print(z(r))
# print(z(a))

## CALLING METHODS OF SAME NAME THROUGH INHERITANCE ###
# class Maths:
#     def area(self):
#         pass

#     def perimeter(self):
#         pass

#     def circumference(self):
#         pass

# class Rectangle(Maths):
#     def __init__(self,l,b):
#         self.l = l
#         self.b = b

#     def area(self):
#         return self.l * self.b
    
#     def perimeter(self):
#         return 2*(self.l * self.b)
    
# class Square(Maths):
#     def __init__(self, a):
#         self.a = a
    
#     def area(self):
#         return self.a * self.a
    
#     def perimeter(self):
#         return 4 * self.a
    
# class Circle(Maths):
#     def __init__(self,radius):
#         self.radius = radius
    
#     def circumference(self):
#         return 2*3.14*self.radius
        
# x = [Rectangle(10,2) , Square(5)]
# y = [Circle(5)]

# for result in x:
#     print(result.area())

# for result in x:
#     print(result.perimeter())

# for result in y:
#     print(result.circumference())

### ABSTRACT BASE CLASS IN POLYMORPHISM ###
# from abc import ABC , abstractmethod

# class NSTI(ABC):
#     @abstractmethod
#     def xyz(self):
#         pass

# class AI(NSTI):
#     def xyz(self):
#         return "ARTIFICIAL INTELLIGENCE"
    
# class CHNM(NSTI):
#     def xyz(self):
#         return "COMPUTER HARDWARE NETWORKING AND MAINTAINENCE"
    
# x = [AI() , CHNM()]

# for value in x:
#     print(value.xyz())

# Demonstrate calculating the area of diff shapes using abstract base class 
# from abc import ABC, abstractmethod
# class Cal_area(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Cal_area):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         print(f"Area of circle is : {3.14*self.radius**2}")
        
# class Triangle(Cal_area):
#     def __init__(self, l, h):
#         self.l = l
#         self.h = h

#     def area(self):
#        print(f"Area of Triangle is : {0.5*(self.l*self.h)}")

# class Square(Cal_area):
#     def __init__(self, a):
#         self.a = a

#     def area(self):
#         print(f"Area of Square is : {self.a**2}")
    
# class Rectangle(Cal_area):
#     def __init__(self, l, b):
#         self.l = l
#         self.b = b

#     def area(self):
#         print(f"Area of Rectangle is : {self.l*self.b}")
    
# x = [Circle(5), Triangle(8,10), Square(4), Rectangle(10,2)]

# for result in x:
#     result.area()
    

# Write a code for Abstract class where you are building a restaurant ordering system. The menu includes main courses, beverages, and desserts. Each item has a different preparation time and pricing model.
# from abc import ABC, abstractmethod
# class Restaurant:
#     @abstractmethod
#     def prep_time(self,time):
#         pass

#     @abstractmethod
#     def price(self,amount):
#         pass    

# class MainCourse(Restaurant):
#     def prep_time(self, time):
#         self.time = time
#         print(f"Your dish will be prpared in {self.time} minutes.")

#     def price(self,amount):
#         self.amount = amount
#         print(f"cost of the dish is : {self.amount}")

# class Beverages(Restaurant):
#     def prep_time(self, time):
#         self.time = time
#         print(f"Your beverage will be prpared in {self.time} minutes.")
        
#     def price(self, amount):
#         self.amount = amount
#         print(f"cost of the dish is : {self.amount}")

# class Desert(Restaurant):
#     def prep_time(self, time):
#         self.time = time
#         print(f"Your dish will be prpared in {self.time} minutes.")

#     def price(self, amount):
#         self.amount = amount
#         print(f"cost of the dish is : {self.amount}")

# x = [MainCourse(), Beverages(), Desert()]
# for item in x:
#     item.prep_time(10)
#     item.price(200)




