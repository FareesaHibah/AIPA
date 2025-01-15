                            ### EXCEPTIONAL HANDLING ###
# Write a Python program that defines a custom exception NegativeNumberError. Raise this exception if the user inputs a negative number and handle it gracefully.
# class NegativeNumberError(Exception):
#     pass
#
# try:
#     x=int(input("Enter a number: "))
#     if(x<0):
#         raise NegativeNumberError("Negative!")
#     print("The number you entered is positive: ",x)
# except NegativeNumberError:
#     print("Number is negative.")


# Write a Python program that takes two numbers as input and performs division. Handle the case where the divisor is zero using exception handling.
# try:
#     x=int(input("Enter a number: "))
#     y=int(input("Enter another number: "))
#     z=x/y
#     print(z)
# except ZeroDivisionError:
#     print("Cannot divide by zero.")


# Write a Python program that tries to read a file specified by the user. Handle the case where the file does not exist.
# try:
#     x=input("Enter the file name: ")
#     with open(x,"r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File does not exist!")



                            ### FILE HANDLING ###
# Write a Python program that reads the first 10 characters from a file, then moves the pointer to the 5th character and reads the next 10 characters.
# file=open("AI.txt","r")
# with open("AI.txt","r") as file:
#     print("Before seeking: ",file.read(10))
#     file.seek(5)
#     print("After seeking to 5th place: ",file.read(10))


# Write a Python program that reads content from one file and writes it to another file.
# with open("AI.txt","r") as file:
#     con=file.read()
# with open("123.txt","w") as file:
#     file.write(con)


# Write a Python program to count the number of lines, words, and characters in a given file.
# with open("AI.txt","r") as file:
#     lines=file.readlines()
#     len_line=len(lines)
#     print("No.of lines are: ",len_line)
#
# with open("AI.txt","r") as file:
#     words=file.read()
#     len_word=len(words.split())
#     print("No.of words are: ",len_word)
#
# with open("AI.txt","r") as file:
#     char=file.read()
#     len_char=len(char)
#     print("No.of characters are: ",len_char)


# Write a Python program that appends log messages with timestamps to a log file.
# import datetime
#
# def append_log(message, file_name="AI.txt"):
#     time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     log_entry = f"{time} - {message}\n"
#     with open(file_name, "a") as file:
#         file.write(log_entry)
#     print(log_entry.strip())
#
# append_log("Application started")
# append_log("User logged in")

