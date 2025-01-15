# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod 
#     def start(self):
#         pass

#     @abstractmethod
#     def working(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass

# class Bike(Vehicle):
#     def start(self):
#         print("Hello!")
    
#     def stop(self):
#         print("Bye!")

# class Car(Vehicle):
#     def start(self):
#         print("Car is switched on")

#     def stop(self):
#         print("Car is switched off..")

# x=Car()
# x.start()
# x.working()        
# x.stop()


# from abc import ABC , abstractmethod
# class Math(ABC):

#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass

# class Square(Math):
#     def __init__(self,side):
#         self.side=side

#     def area(self):
#         return self.side*self.side

#     def perimeter(self):
#         return 4*self.side
    
# class Rectangle(Math):
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b

#     def area(self):
#         return self.l*self.b
    
#     def perimeter(self):
#         return 2*(self.l+self.b)
    
# x=Square(10)
# y=Rectangle(10,2)

# print(f"Area of the square : {x.area()}")
# print(f"Perimeter of the square : {x.perimeter()}")

# print(f"Area of the rectangle : {y.area()}")
# print(f"Perimeter of the rectangle : {y.perimeter()}")

# from abc import ABC , abstractmethod

# class BankAccount(ABC):

#     @abstractmethod
#     def deposit(self):
#         pass

#     @abstractmethod
#     def withdraw(self):
#         pass

#     @abstractmethod
#     def check(self):
#         pass


# class Savings(BankAccount):
#     def __init__(self,balance=0):
#         self.balance=balance

#     def deposit(self,money):
#         if money>0:
#             self.balance+=money
#             print(f"{money} added to the account.")
#         else:
#             print(f"{money} could not be added.")
    
#     def withdraw(self,money):
#         if money<=self.balance:
#             self.balance-=money
#             print(f"Withdrew : {money} ")
#         else:
#             print("Not enough balance.")

#     def check(self):
#         print(f"Your balance is : {self.balance}")

# class Credit(BankAccount):
#     def __init__(self,balance=0):
#         self.balance=balance

#     def deposit(self,money):
#         if money>0:
#             self.balance+=money
#             print(f"{money} added to the account.")
#         else:
#             print(f"{money} could not be added.")
    
#     def withdraw(self,money):
#         if money<=self.balance:
#             self.balance-=money
#             print(f"Withdrew : {money} ")
#         else:
#             print("Not enough balance.")

#     def check(self):
#         print(f"Your balance is : {self.balance}")
        
# class Current(BankAccount):
#     def __init__(self,balance=0):
#         self.balance=balance

#     def deposit(self,money):
#         if money>0:
#             self.balance+=money
#             print(f"{money} added to the account.")
#         else:
#             print(f"{money} could not be added.")
    
#     def withdraw(self,money):
#         if money<=self.balance:
#             self.balance-=money
#             print(f"Withdrew : {money} ")
#         else:
#             print("Not enough balance.")

#     def check(self):
#         print(f"Your balance is : {self.balance}")
        

# x=Savings()
# x.deposit(100000)
# x.withdraw(1000)
# x.check()

# y=Credit()
# y.deposit(200000)
# y.withdraw(1000)
# y.check()

# z=Current()
# z.deposit(300000)
# z.withdraw(1000)
# z.check()

