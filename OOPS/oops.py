# class is a collection of objects which lets the object to behave or have properties according to the requirements

# class ai:
#     institute="NSTI" ## ATTRIBUTE ##

#     def __init__(self,name,age,address):
#            self.name= name
#            self.age=age
#            self.address=address

# students=ai("Fareesa",19,"Hyd")
# print(students.name)
# print(f"NAME: {students.name}, AGE: {students.age}, ADDRESS: {students.address}")



# class library:
#     place="State Central Library"

#     def __init__(self,title,genre,year):
#         self.title=title
#         self.genre=genre
#         self.year=year
# book=library("Wings of Fire","Self-help",2005)
# book1=library("Autobiography","Self-help",2015)
# print(f"{book.title},{book.genre},{book.year}")
# print(f"{book1.title},{book1.genre},{book1.year}")


# class india:

#     def __init__(self,state,unionterritory,district):
#         self.state=state
#         self.unionterritory=unionterritory
#         self.district=district
# a=india("Telangana","","")
# print(a.state)
# b=india("","Daman and Diu","")
# print(b.unionterritory)
# c=india("","","Hyderabad")
# print(c.district)


# class car:
    # a="Vehicle"                     ### ATTRIBUTE ###
    # b="Car"
    
    # def xyz(self):
    #     print("Hello: ",self.a)      ### METHOD ###
    #     print("Hello: ",self.b)
    
    # def abc(self):                   ### METHOD ###
    #     print("All the vehicles.")
    
    # def add(self,c,d):
        # print("Sum is:",c+d)
    
    # def sub(self,c,d):
    #     print("Difference is: ",c-d)
    
    # def mul(self,c,d):
    #     print("Product is: ",c*d)
    
    # def div(self,c,d):
    #     print("Result is: ",c/d)
    
# x=car()
# print(x.a)
# print(x.b)
# x.xyz()
# x.abc()
# x.add("Fareesa ","Hibah")
# x.sub(100,20)
# x.mul(100,20)
# x.div(100,20)

####################################################################################################################################################
# class Wallet:
#     def __init__(self,name,balance=0):
#         self.name=name
#         self.balance=balance

#     def add_money(self,money):
#         if money>0:
#             self.balance+=money
#             print(money,"added successfully ")
#         else:
#             print(money,"cannot be added")
    
#     def spend_money(self,money):
#         if money>self.balance:
#             print("Not enough balance.")
#         else:
#             original_balance=self.balance
#             self.balance-=money
    #         print(f"{money} spent from {original_balance}. Remaining balance: {self.balance}")

    # def check(self):
    #     print(f"{self.name}'s balance is: {self.balance}")

# x=Wallet("Fareesa",200)
# y=Wallet("Hibah")

# x.add_money(1800)
# x.check()
# y.add_money(4000)
# y.check()
# x.spend_money(200)
# x.check()
# y.spend_money(1000)
# y.check()


# class flipkart:
#     def __init__(self,item,price,):
#         self.item=item
#         self.price=price
#         self.cart=[]
    
#     def add(self,price=0):
#         if price>0:
#             self.cart.append(self.item)
#             print(f"{self.item} added to cart")
#         else:
#             print(f"{self.item} cannot be added.")
    
#     def view(self):
#         if self.cart:
#             print("Items in the cart: ")
#         for item in self.cart:
#            print(item)
    
#     def remove(self):
#         rem_item=input("Enter the item to be removed: ")
#         if rem_item in self.cart:
#             self.cart.remove(rem_item)
#             print(f"{rem_item} has been removed from the cart.")
#         else:
#             print(f"Could not find {rem_item}")
    
#     def review(self):
#         if self.cart:
#             print("Items in the cart: ")
#             for item in self.cart:
#                 print(item)
#         else:
#             print("Cart is empty.")
    
# x=flipkart("book",50)
# y=flipkart("watch",100)
# x.add(50)
# y.add(100)
# x.view()
# y.view()
# x.remove()
# y.remove()
# x.review()
# y.review()

##########################################################################################################################################################################

