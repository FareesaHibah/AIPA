#  “Checking if a number is positive, zero, or negative using nested if”
# n=int(input("Enter a number: "))
# if(n>=0):
#     if(n==0):
#         print("The number 2is zero.")
#     else:
#         print(n,"is a positive number.")
# else:
#     print(n,"is a negative number.")


# Write a Python program to sum two integers read by user. However, if the sum is between 10 and 20 it will print 15. else print 0
# x=int(input("Enter a number: "))
# y=int(input("Enter another number: "))
# z=x+y
# if(10<=z<=20):
#     print("The sum is 15.")
# else:
#     print("The sum is zero.")


# Create two boolean objects and Use the and operator in an if statement
# bool1=True
# bool2=False
# if(bool1 and bool2):
#     print("Both statements are true.")
# else:
#     print("Atleast one statement is false.")    

# # Implement the python code for Convert temperatures to and from celsius, fahrenheit
# temp=input("Enter the temperature you want to convert(eg.37C,100F): ")
# degree=int(temp[:-1])
# i_convention=temp[-1]
# if(i_convention.upper()=="C"):
#     result=int(round((9*degree)/5+32))
#     o_convention="Farenheit"
# elif(i_convention.upper()=="F"):
#     result=int(round((degree-32)*5/9))
#     o_convention="Celcius"
# else:
#     print("Enter proper convention.")
#     quit()
# print("The temperature in",o_convention,"is",result,"degrees")    


# Write a Python program to convert a month name to a number of days.
# mn=input("Enter the month name: ").lower()
# if(mn=="january" or mn=="march" or mn=="may" or mn=="july" or mn=="august" or mn=="october" or mn=="december"):
#     print("No.of days in",mn,"are 31.")
# elif(mn=="april" or mn=="june" or mn=="september" or mn=="november"):
#     print("No. of days in",mn,"are 30.")
# elif(mn=="february"):
#     print("No.of days in",mn,"are 28.")
# else:
#     print("Invalid month name.")

# Implementation of itrative statements - for loop
# Task 1: Using a for loop to iterate over each character
# x="Fareesa Hibah"
# for letter in x:
#     print(letter)

# Task 2: Using range to iterate from 0 to 4
# for i in range(5):
#     print(i)

