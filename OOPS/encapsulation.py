# PUBLIC 
# class AI:
#     def __init__(self):
#         self.name="Fareesa"
    
#     def data(self):
#         print(f"NAME:{self.name}")

# x=AI()
# x.data()
# print(x.name)

#PROTECTED
# class NSTI:
#     def __init__(self):
#         self._trade="AI"

# class CTS(NSTI):
#     def disp(self):
#         print(self._trade)

# x=CTS()
# x.disp()
# print(x._trade)   ### GIVES ERROR

# #PRIVATE
# class gmail():
#     def __init__(self):
#         self.__password="1234"

#     def disp(self):
#         print(f"Your passwod is:{self.__password}")

# x=gmail()
# x.disp()
# print(x._password) #### GIVES ERROR
####
# class employee():
#     def __init__(self):
#         self.__salary="200000"

#     def displ(self):
#         print(f"Salary is:{self.__salary}")
    
# x=employee()
# x.displ()
# print(x.__salary)  ### GIVES ERROR




# class hospital():
#     def __init__(self):
#         self.__name=[]

#     def add(self,name):
#         self.__name.append(name)
#         print(f"Patient name:{self.__name} has been added.")

#     def rem(self,name):
#         if name in self.__name:
#             self.__name.remove(name)
#             print(f"Patient name:{self.__name} removed.")
#         else:
#             print(f"Patient name:{self.__name} could not be found.")
    
#     def view(self):
#         for name in self.__name:
#             print(name)
# x=hospital()
# x.add("A")
# x.add("B")
# x.add("C")
# x.view()





# class AI():
#     def __init__(self):
#         self.__student=[]

#     def add(self,student):
#         self.__student.append(student)
#         print(f"{student} has been added.")

#     def rem(self,student):
#         if student in self.__student:
#             self.__student.remove(student)
#             print(f"{student} has been removed.")
#         else:
#             print(f"{student} could not be found.")

#     def view(self):
#         for student in self.__student:
#             print(student)

# x=AI()
# x.add("Fareesa")
# x.add("Hibah")
# x.add("Ayesha")
# x.rem("Fareesa")
# x.view()




# Implementation of encapsulation in a BankAccount transaction
# class BankAccount:
#     def __init__(self,name,acc_no,balance=0):
#         self.name=name
#         self._acc_no=acc_no
#         self.__balance=balance

#     def deposit(self,money):
#         if money>0:
#             self.__balance+=money
#             print(f"Rupees {money} deposited in the account.")
#         else:
#             print(f"{money} cannot be deposited.")

#     def withdraw(self,money):
#         if money<=self.__balance:
#             self.__balance-=money
#             print(f"Rupees {money} withdrew from the account.")
#         else:
#             print(f"Not enough balance.")

#     def check(self):
#         print(f"Your balance is:{self.__balance}")

# x=BankAccount("Fareesa",123425241324)
# x.deposit(10000)
# x.withdraw(100)
# x.check()

##########################################################################################

# class Movie():
#     def __init__(self,id,title,price):
#         self.id=id
#         self.__title=title
#         self.__price=price 
    
#     def set_title(self,title):
#         self.__title=title

#     def set_price(self,price):
#         if price>0:
#             self.__price=price
#         else:
#             print("Enter correct amount.")
    
#     def get_title(self):
#         return self.__title

#     def get_price(self):
#         return self.__price
    
#     def disp(self):
#         print(f"ID : {self.id}")
#         print(f"NAME : {self.__title}")
#         print(f"PRICE : {self.__price}")
    
# def movie():
#     id=input("Enter id: ")
#     title=input("Enter movie name: ")
#     while True:
#         price=int(input("Enter the price: "))
#         if price>0:
#             break
#         else:
#             print("Price must be more than 0")
        
#     return Movie(id,title,price)

# x=movie()
# x.disp()

# print(f"Title : {x.get_title()}")
# print(f"Price : {x.get_price()}")