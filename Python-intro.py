# me="Fareesa" 
# print(me)

# x=235
# print(x)

# f=1.344
# print(f)

# import keyword

# keywords=keyword.kwlist

# print(keywords)

# x="""xdfgyuiobjhwfhfjhcbgdtrewiofjcn dfubv
# fhjcgrfygevcnduisxanhdngyownx
# ncxfdgbr7832780bcykuxandghdu"""
# print(x)

# x=10/2
# print(x)

# print(10%2)

# x=10
# y=3
# z=x/y
# print(z)
# single slash gives an approximate value (decimal)

# x=10
# y=3
# z=x//y    
# print(z)
# floor division gives an exact or whole value (quotient)

# x=10
# y=3
# z=x%y
# print(z)
# this (%) gives the remainder

# x="FAREESA"
# y=" HIBAH <3"
# print(x+y)
# Concatenate is used here

# x=10
# y=1.7
# print(x+y)

# x=100
# y=99
# print(x-y)

# x="Fareesa"
# y="Hibah"
# print(x[1:6])
# index always starts from 0. 

# x=1
# y=1.2
# z="AROHI"
# print(type(x))
# print(type(y))
# print(type(z))

# print(2==3)
# print(1>2)
# print(2<3)
# print(2==2)

# x="fareesa"
# a="fareesa"
# print(x==a)

# x=["fareesa","adil","ramesh","arkaan"]
# x.append("AROHI")
# print(x) 
# lists are made in square brackets
# append is used to add another name to the list but in the end
# insert is used to add a name to the list at a specific place
# x.insert(2,"me")
# print(x)
# x.insert(4,"7")
# print(x)
# x.insert(4,"6")
# print(x)

# y=["sakshi","hibah","daya","hello"]
# x.extend(y)
# print(x)
# extend is used to merge two lists together

# y=["sakshi","hibah","daya","hello"]
# y.remove("hello")
# print(y)
# remove is used when we know the values in the list 

# x=["sakshi","hibah","daya","hello"]
# del x[1]
# print(x)
# delete is used when we don't know the values in the list

# x=["sakshi","hibah","daya","hello"]
# del x
# print(x)
# # this shows error because the list x that we defined is deleted so it cannot be printed

# y=["sakshi","hibah","daya","hello"]
# y.clear()
# print(y)
# # clear is used to delete the entire list

# x=["fareesa","adil","ramesh","arkaan"]
# y=["sakshi","hibah","daya","hello"]
# x.clear()
# y.clear()
# print(x)
# print(y)

# x=["fareesa","adil","ramesh",56,76,"arkaan"]
# print(type(x)) 

# x=("fareesa","adil","ramesh",56,76,"arkaan")
# print(type(x))
# x[2]="Hello"
# print(x)
# # the above is in tuple format. Tuple cannot be extended or edited

# x=("fareesa","adil","ramesh",56,76,"arkaan")
# y=list(x)
# y[2]="arohi"
# x=tuple(y)
# print(x)

# x=("fareesa","adil","ramesh","arkaan")
# y=("hibah",)
# x +=y
# print(x)
# # this is used to add something to the tuple list

# print("Hey Ayesha!")


# x=["Believe",10,"you",20,"can"]
# del x[1]
# del x[2]
# print(x)

# x="Believe you can and you're halfway there"
# print(x.count("a"),x.count("e"),x.count("i"),x.count("o"),x.count("u"))


# x=[1,2,3,4,5,6,7,8,9]
# y=sum(x)       # y=x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7]+x[8]
# print(y)


#4) x=int(input("Enter the word: "))
# if (x==x[::-1]):
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")


# var='x'
# check=type(var)
# if(check==str):
#     print(var,"is of type str.")
# else:
#     print(var,"is not of type str.")



# l=(5,10,15)
# if(10 in l):
#     print("10 is in the tuple.")
# else:
#     print("10 is not in the tuple.")


# x=int(int(input("Enter a value:  ")))
# print(type (x))


# x=[]
# n1=int(input("Enter number 1: "))
# x.append(n1)
# n2=int(input("Enter number 2: "))
# x.append(n2)
# n3=int(input("Enter number 3: "))
# x.append(n3)
# n4=int(input("Enter number 4: "))
# x.append(n4)
# n5=int(input("Enter number 5: "))
# x.append(n5)
# s=sum(x)
# print(s)


# x=input("Enter the elements of a list")
# y=list(map(int,x.split()))
# sum=sum(y)
# print(sum)


# x=input("Enter the elements of a list: ")
# y=list(map(int,x.split()))
# y.sort()
# print(y)

# a,b,c=1,2,3
# print(c)


# x=[1,1,2,2,3,3,4,"hi"]
# x.remove(1)
# x.remove(2)
# x.remove(3)
# print(x)

# x=input("Enter the elements of a list")
# y=list(map(int,x.split()))
# y.sort()
# print(y)


# x=int(input("Enter a no: "))
# print(x,"lies between 10 and 20.",x>10 and x<20)


#temp = input("Enter the temperature you want to convert (e.g., 37C, 100F): ")
# degree = int(temp[:-1])
# i_convention = temp[-1].upper()

# if i_convention == "C":
#     result = round((9 * degree) / 5 + 32)
#     o_convention = "Fahrenheit"
# elif i_convention == "F":
#     result = round((degree - 32) * 5 / 9)
#     o_convention = "Celsius"
# else:
#     print("Enter a proper convention.")
#     quit()

# print(f"The temperature in {o_convention} is {result} degrees")

# class GasoverError(Exception):
#     pass

# class NoTeaPowder(Exception):
#     pass

# class UnexpectedGuestError(Exception):
#     pass

# def prepare_tea():
#     try:
#         gas = get_gas()
#         powder = get_powder()
#         serve_tea(powder)
#     except GasoverError:
#         print("Oops! Gas is over.")
#     except NoTeaPowder:
#         print("Tea powder is over.")
#     except UnexpectedGuestError:
#         print("We have more guests.")
#     else:
#         print("Tea is prepared, acchi ya buri.")

# def get_gas():
#     user_input = input("Enter 'yes' if gas is finished, otherwise 'no': ").strip().lower()
#     if user_input == "yes":
#         raise GasoverError("Oops! Gas is over.")
#     return "gas"

# def get_powder():
#     user_input = input("Enter 'over' if the tea powder is over, otherwise 'no': ").strip().lower()
#     if user_input == "over":
#         raise NoTeaPowder("Tea powder is over.")
#     return "powder"

# def serve_tea(powder):
#     user_input = input("Enter 'extra' if there are unexpected guests, otherwise 'no': ").strip().lower()
#     if user_input == "extra":
#         raise UnexpectedGuestError("We have more guests.")
#     print("Chai is ready! Enjoy!")

# prepare_tea()







# import datetime
# def append_log(message,file_name="AI.txt"):
#     time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     log_entry=time,"-",message
#     with open(file_name,"a") as file:
#         file.write(log_entry)
#     print("Log entry added: ",log_entry.strip())

# append_log("Application started")
# append_log("User logged in")



# f'Title of the book: {title},Author is: {author},Price of the book: {price}\n'




# def search_book(filename):
#     try:
#         if os.path.exists(filename):
#             with open (filename,"r") as file:
#                 books=file.readlines()
#                 if books:
#                     print("Inventory: ")
#                     for book in books:
#                         try:
#                             title,author,price=book.strip().split(",")
#                             print(f'Title of the book: {title},Author is: {author},Price of the book: {price}\n')
#                         except ValueError:
#                             print(f'Skipping malfunction line {book.strip()}')
#                 else:
#                     print("Inventory is empty.")
#         else:
#             print("Book not found.")
#     except Exception as e:
#         print(f'An error occurred: {e}')


# def save(filename,contacts):
#     try:
#         with open(filename,"a") as file:
#             for contact in contacts:
#                 file.write(f"{contact['name']},{contact['number']}\n")
#         print("Contacts have been saved.")
#     except Exception as e:
#         print("An error occurred: ",e)

# num=int(input("Enter a number: "))
# try:
#     x=num/0
#     print(x)
# except ZeroDivisionError:
#     print("Number cannot be divided by zero.")
# try:
#     num=int(input("Enter a value: "))
#     print(num)
# except ValueError:
#     print("Cannot be converted into int.")


# class AgeError(Exception):
#     pass
# try:
#     x=int(input("Enter your age: "))
#     if x<18:
#         raise AgeError()
#     else:
#         print("You are eligible to vote.")
# except AgeError:
#     print("You are not eligible to vote")
    

    
# x="hi\n"
# print(x*3)


# my_module.py

# def main():
#     print("This is the main function.")

# def greeting():
#     print("Hello!")

# if __name__ == "__main__":
#     main()


