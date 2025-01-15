# import module
# a=5
# b=6
# print(module.add(a,b))

# import module 
# a=10
# b=2
# print(module.sub(a,b))





### EXCEPTIONAL HANDLING IN PYTHON ###

# try:
#     result=10/0
# except ZeroDivisionError:
#     print("Number cannot be divided by zero.")

# try:
#     x=10/2
# except ZeroDivisionError:
#     print("You can't divide a number by zero.")
# else:
#     print("Result is:",x)   ### ELSE IS USED TO EXECUTE A CODE WITH DOES NOT HAVE ANY ERRORS ###

# try:
#     x==10
# except NameError:
#     print("Write the correct syntax.")
# else:
#     print("The value is:",x)

# try:
#     x=10/0
# except ZeroDivisionError:
#     print("You can't divide a number by zero.")
# else:
#     print("Result is:",x)  
# finally:          ### "FINALLY" STATEMENT WILL BE PRINTED REGARDLESS OF THE ERROR. IT HAS NO RELATION WITH THE ABOVE STATEMENTS. ###
#     print("This will print regardless of the error.")

# x=10
# if(x%2==0):
#     print("EVEN")
# else:
#     print("ODD")
# finally:
# print("hi")

def check_age(age):
    if age<18:
        raise ValueError("Age must be atleast 18.")
    return "You are eligible to vote."
try:
    check_age(18)
except ValueError as ve:
    print(ve)

# try:
#     num=int(input("Enter a number: "))
#     result=10/num
# except ValueError:
#     print("Invalid input.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# else:
#     print(result)

# class GasoverError(Exception):
#     pass
# class NoTeaPowder(Exception):
#     pass
# class UnexpectedGuestError(Exception):
#     pass

# def prepare_tea():
#     try:
#         gas=get_gas()
#         powder=get_powder()
#         serve_tea(powder)
#     except GasoverError:
#         print("Oops! Gas is over.")
#     except NoTeaPowder:
#         print("Tea powder is over.")
#     except UnexpectedGuestError:
#         print("We have more guests.")
#     finally:
#         print("Code is executed.")

# def get_gas():
#     user_input=input("Enter 'yes' if gas is finished, otherwise 'no': ").strip().lower()
#     if user_input=="yes":
#         raise GasoverError("Oops! Gas is over.")
#     return "gas"

# def get_powder():
#     user_input=input("Enter 'over' if the tea powder is over, otherwise 'no': ").strip().lower()
#     if user_input=="over":
#         raise NoTeaPowder("Tea powder is over.")
#     return "powder"

# def serve_tea(powder):
#     user_input=input("Enter 'extra' if there are unexpected guest, otherwise 'no': ").strip().lower()
#     if user_input=="extra":
#         raise UnexpectedGuestError("We have more guests.")
#     print("Chai is ready!,Enjoy!")

# prepare_tea()

