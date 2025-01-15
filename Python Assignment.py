                                                   # PYTHON ASSIGNMENT 
# Python Keywords and Identifiers:- 

#1) 	Identify the invalid identifier from the following: my_var, _myVar, 2var, my-var.
#  my_var=2
# print(my_var) # is valid identifier.
# _myVar=2
# print(_myVar) # is valid identifier.
# 2var=2
# print(2var) # is invalid identifier. 
# my-var=2
# print(my-var) # is invalid identifier.

#2) 	List 5 Python keywords that cannot be used as identifiers.
# elif,if,del,remove,else cannot be used as identifiers.



# Python Print Function:-

#1) 	Write a program to print "Welcome to Python Programming!".
# x="Welcome to Python Programming"
# print(x)

#2) 	Use the print() function to display: Your name and Your favorite number
# x="Fareesa Hibah"
# y="2"
# print(x,y)



# Python Variables:-

#1) 	Assign the value 25 to a variable and print it.
# x=25
# print(x)

#2) 	Swap two variables without using a temporary variable.
# x=1
# y=2
# print("x","=",x,"y","=",y)
# x=y
# y=1
# print("x","=",x,"y","=",y)

# 3) 	Assign three values to three variables in a single line.
# a, b, c = 1, 2, 3
# print(a,b,c)



# Python Data Types:-

#1) 	Determine the data type of the following values: 10 , 10.5 , "Hello" , True
# a=10
# b=10.5
# c="Hello"
# d=True
# print(type(a)) # int
# print(type(b)) # float
# print(type(c)) # str
# print(type(d)) # bool

#2) 	Check whether the variable x is of type str.
# var='x'
# check=type(var)
# print(var,"is of type str",check==str)



# Python Numbers:-

#1) 	Write a program to add two integers.
# x=1
# y=2
# z=x+y
# print(z)

#2) 	Find the remainder when 25 is divided by 4.
# x=25
# y=4
# z=x%y
# print(z)

#3) 	Calculate the square of a number using an operator.
# x=2          #3) x=11
# y=x*x          # y=x**2
# print(y)       # print(y)



# Python Strings:-

#1) 	Create a string and print its length.
# x="Believe you can and you will!"
# print(len(x))

#2) 	Write a program to slice a string: Extract "World" from "Hello World".
# x= "Hello World"
# slice=x[6:11]
# print(slice)

#3) 	Convert the string "python programming" to uppercase.
# x="python programming"
# y=x.upper()
# print(y)

#4) 	Concatenate two strings: "Hello" and "Python".
# x="Hello"
# y=" Python"
# z=x+y
# print(z)

#5) 	Use an escape character to print He said, "Python is fun!".
# x="He said, \"Python is fun!\""
# print(x)



# Python Lists:-

#1) 	Create a list with 5 elements and print the third element.
# x=[1,2,3,4,5]
# y=x[2]
# print(y)

#2) 	Replace the second element in the list [1, 2, 3, 4, 5] with 10.
# x=[1,2,3,4,5]
# x[2]=10
# print(x)

#3) 	Add a new item to the end of the list [10, 20, 30].
# x=[10,20,30]
# x.append("100")
# print(x)

#4) 	Remove the element 20 from the list [10, 20, 30].
# x=[10,20,30]
# x.remove(20)
# print(x)

#5) 	Sort the list [5, 1, 8, 3] in ascending order.
# x=[5, 1, 8, 3] 
# x.sort()
# print(x)



# Python Operators:-

#1) 	Demonstrate the use of arithmetic operators in Python.
# x=10
# y=22
# z=x+y #ADDITION
# print(z)

# x=10
# y=22
# z=x-y #SUBTRACTION
# print(z)

# x=7
# y=5
# z=x*y #MULTIPLICATION
# print(z)

# x=10
# y=3
# z=x/y #DIVISION
# print(z)

# x=10
# y=3
# z=x//y #FLOOR DIVISION
# print(z)

# x=10
# y=3
# z=x%y #MODULUS
# print(z)

# x=2
# y=3
# z=x**y #EXPONENTIATION
# print(z)

#2) 	Write a program to compare two numbers and print the larger one.
# x=int(input("Enter a number"))
# y=int(input("Enter another number"))
# if(x>y):
#     print(x,"is greater")
# else: 
#    print(y,"is greater")

#3) 	Combine logical operators to check if a number is greater than 10 and less than 20.
# x=int(input("Enter a number"))                         #3) x=int(input("Enter a no: "))
# if(x>10 and x<20):                                           print(x,"lies between 10 and 20.",x>10 and x<20)
#     print(x,"lies between 10 and 20.",)
# else:
#     print(x,"does not lie between 10 and 20.")



# Python Booleans:-

#1) 	Write a program that returns True if a number is even, and False otherwise.
# x=int(input("Enter a number"))
# print(x,"is even",x%2==0)

#2) 	Use the bool() function to check the truth value of an empty list.
# l=[]
# check=bool(l)
# print(check)



# Input and Output:-   

#1) 	Write a program that asks for the user's name and prints a greeting.
# x=input("Please enter your name: ")
# print("Hello",x,"!","Welcome to Python Programming!")

#2) 	Take two numbers as input from the user and display their sum.
# x=int(input("Enter a number: "))
# y=int(input("Enter another number: "))
# z=x+y
# print("their sum is",z)



# Python Variables:-

#1) 	Assign a float value to a variable and print it.
# f=67.56
# print(f)

#2) 	Assign the result of 10 + 20 to a variable and display it.
# s=10+20
# print(s)



# Python Type Conversion:-

#1) 	Convert an integer to a float and print it.
# x=56
# y=float(x)
# print(y)

#2) 	Convert a string "123" to an integer and add 10 to it.
# x="123"
# y=int(x)+10
# print(y)



# Python Strings:-

#1) 	Find the index of the first occurrence of the character "o" in "Hello World".
# x="Hello World"
# index=x.find("o")
# print(index)

#2) 	Replace "World" with "Python" in "Hello World".
# x="Hello World"
# y=x.replace("World","Python")
# print(y)

#3) 	Reverse the string "Python".
# x="Python"
# y=x[::-1]
# print("The reversed string is: ",y)

#5) 	Check whether the string "madam" is a palindrome.
# x="madam"
# if(x==x[::-1]):
#     print(x,"is a palindrome.")
# else:
#     print(x,"is not a palindrome.")



# Python Lists:-

#1) 	Create a list with elements of different data types.
# x=[1,2.9,"Fareesa",True]
# print(x)

#2) 	Write a program to find the sum of all numeric elements in a list.
# x=[1,2,3,4,5]
# print(sum(x))

#3) 	Remove all occurrences of the number 5 from the list [5, 10, 15, 5, 20].
# x=[5, 10, 15, 5, 20]
# del x[0]
# del x[2]
# print(x)

#5) 	Write a program to merge two lists.
# x=["a","b","c","d","e"]
# y=["f","g","h","i","j"]
# z=x+y
# print(z)



# Python Tuples:-

#1) 	Create a tuple with 4 elements and print the second element.
# x=(131,5,6,3,534,43)
# print(x[1])

#2) 	Convert the tuple (1, 2, 3, 4) into a list.
# x=(1, 2, 3, 4) 
# print(list(x))

#3) 	Write a program to unpack a tuple into individual variables.
# x=(1,2,3,4,5)
# a,b,c,d,e=x
# print(a,b,c,d,e)

#4) 	Check if the element 10 is present in the tuple (5, 10, 15).
# l=(5,10,15)
# print("10 is in the tuple.",10 in l)



# Strings:-

#1) 	Write a program to reverse a string entered by the user.
# x=input("Enter the string: ")
# y=x[::-1]
# print("Reversed string is:",y)

#3) 	Take two strings as input and concatenate them.
# x=input("Enter a string: ")
# y=input("Enter another string: ")
# print(x+y)

#4) 	Write a Python program to check if a string is a palindrome.
# x=input("Enter the word: ")
# if (x==x[::-1]):
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

#5) 	Ask the user for their full name and print it in uppercase.
# x=input("Enter your full name: ")
# y=x.upper()
# print("Your name in uppercase would be: ",y)

#6) 	Write a program to replace all spaces in a sentence with underscores.
# x="Believe you can and you're halfway there"
# y=x.replace(" ","_")
# print(y)

#7) 	Input a string and find the first occurrence of the letter 'a'.
# x="Believe you can and you're halfway there"
# y=x.find("a")
# print(y)

#8) 	Write a program to split a sentence into words and print each word on a new line.
# x="Believe \n you \n can \n and \n you're \n halfway \n there"
# print(x)



# Lists:-

#1) 	Write a program to find the sum of all numbers in a list provided by the user.
# x=[]                                       1) x=input("Enter the elements of a list")
# n1=int(input("Enter number 1: "))               y=list(map(int,x.split()))
# x.append(n1)                                    sum=sum(y)
# n2=int(input("Enter number 2: "))               print(sum)
# x.append(n2)
# n3=int(input("Enter number 3: "))
# x.append(n3)
# n4=int(input("Enter number 4: "))
# x.append(n4)
# n5=int(input("Enter number 5: "))
# x.append(n5)
# s=sum(x)
# print(s)

#2) 	Take a list of numbers as input and sort it in ascending order.
# x=[]                                      2) x=input("Enter the elements of a list")
# n1=int(input("Enter number 1: "))              y=list(map(int,x.split()))
# x.append(n1)                                   y.sort() 
# n2=int(input("Enter number 2: "))              print(y)
# x.append(n2)
# n3=int(input("Enter number 3: "))
# x.append(n3)
# n4=int(input("Enter number 4: "))
# x.append(n4)
# n5=int(input("Enter number 5: "))
# x.append(n5)
# x.sort()
# print(x)

#3) 	Write a script to remove all duplicates from a list.
# x=[1,1,2,2,3,3,4,"hi"]
# x.remove(1)
# x.remove(2)
# x.remove(3)
# print(x)

#5) 	Write a program to check if a list contains a specific element entered by the user.
# x=input("Enter the elements of a list: ")
# l=x.split()
# y=input("Element to check for: ")
# if(y in x):
#     print(y,"is in the list.")
# else:
#     print(y,"is not in the list.")

#6) 	Ask the user for five numbers, store them in a list, and find the average.
# x=input("Enter any five numbers: ")
# y=list(map(int,x.split()))
# avg=(sum(y))/5
# print("The average of the numbers is:",avg)

#8)  	Input a list and reverse its elements using slicing.
# x=input("Enter the numbers: ")
# y=list(map(int,x.split()))
# print("The reversed list is: ",x[::-1])

#10) 	Take a list of strings as input and convert all strings to uppercase.
# x=input("Enter the strings: ")
# y=x.split()
# z=x.upper()
# print(z)



# User Input:-

#1) 	Write a program to take the user's age as input and print if they are eligible to vote (age >= 18).
# x=int(input("Enter your age: "))
# if(x>=18):
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.",18-x,"years to go")

#2) 	Ask the user for a temperature in Celsius and convert it to Fahrenheit.
# x=int(input("Enter the temperature in degrees celcius: "))
# y=(x*(9/5))+32
# print(x,"in degrees farenhiet is: ",y)

#3) 	Write a program to calculate the Body Mass Index (BMI) based on user input height and weight.
# x=float(input("Enter your weight in kgs: "))
# y=float(input("Enter your height in meters: "))
# z=(x)/(y**2)
# print("Your Body Mass Index is:",z)

#4) 	Take a user's birth year as input and calculate their current age.
# x=int(input("Enter your year of birth: "))
# y=2024-x
# print("You are",y,"years old.")

#6) 	Ask the user to enter a number and print its multiplication table.
# x=int(input("Enter a number: "))
# n=1
# while n<=12:
#     print(x,"*",n,"=",x*n)
#     n+=1

#8) 	Ask the user to input three numbers and calculate their average.
# x=int(input("Enter no 1: "))
# y=int(input("Enter no 2: "))
# z=int(input("Enter no 3: "))
# avg=(x+y+z)/3
# print("The average of",x,",",y,",",z,"is:",avg)

