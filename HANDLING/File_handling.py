# file=open("AI.txt","r")
# content=file.read()
# print(content)
# file.close()

# with open("AI.txt","r") as file:
#    content=file.read()
#    print(content)

# with open("AI.txt","r") as file:
#    for line in file:
#       print(line.strip())

# with open("AI.txt","r") as file:
#    content=file.read(19)
#    print(content)

# with open("AI.txt","r") as file:
#     file.readline(25)
#     content=file.read(19)
#     print(content)

# with open("AI.txt","w") as file:
#     file.write("Good Morning!")

# with open("AI.txt","a") as file:
#     file.write("\n Good day to you! \n This is a new line.")

# with open("AI.txt","r") as file:
#        print(file.tell())

# with open("AI.txt","r") as file:
#     file.read(30)
#     file.read(7)     
#     file.seek(29)     ### SKIPS THE NO.OF CHARACTERS GIVEN ###
#     print(file.read())
#     print(file.tell()) ### GIVES YOU THE CURSOR POSITION ###

# try:
#     with open("AI.txt","r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File is not found.")
# finally:
#     print("The code is executed.")

# import os
# if os.path.exists("123.py"):
#     os.remove("123.py")         ### REMOVE WILL DELETE THE FILE. THAT FILE CANNOT BE RESTORED. ###
#     print("Your file is deleted.")
# else:
#     print("File not found.")

import os
def display_name():
    print("NSTI Book Strore")
    print("1. Add a book: ")
    print("2. View books: ")
    print("3. Search for book: ")
    print("4. Delete")
    print("5. Exit")
# ADD A NEW BOOK #
def new_book(filename):
    try:
        with open (filename,"a") as file:
            title=input("Enter the book title: ")
            author=input("Enter the author name: ")
            price=input("Enter the price of the book: ")
            book=f'{title},{author},{price}\n'
            file.write(book)
            print("Book added successfully!")
    except Exception as e:
        print(f'An error occurred: {e}')

def view_inventory(filename):
    try:
        if os.path.exists(filename):
            with open(filename,"r") as file:
                books=file.readlines()
                if books:
                    print("Inventory: ")
                    for book in books:
                        try:
                            title,author,price=book.strip().split(",")
                            print(f'Title of the book: {title},Author is: {author},Price of the book: {price}\n')
                        except ValueError:
                            print(f'Skipping malfunction line {book.strip()}')
                else:
                    print("Inventory is empty.")
        else:
            print("Inventory file does not exist.")
    except Exception as e:
        print(f'An error occurred: {e}')

def search_book(filename):
    try:
        if os.path.exists(filename):
            search=input("Enter the book name: ").lower()
            with open (filename,"r") as file:
                books=file.readlines()
                found=False
                for book in books:
                    try:
                        title,author,price=book.strip().split(",") 
                        if title==search:
                            print(f'title-{title},{author},{price}')
                            found=True
                            break
                    except ValueError:
                        print(f'Skipping malfunction line {book.strip()}')
                if not found:
                    print("Book not found.")
        else:
            print("Inventory file does not exist.")
    except Exception as e:
        print(f'An error occurred: {e}')

def delete_book(filename):
    try:
        if os.path.exists(filename):
            title1=input("Enter the title of the book: ")
            with open(filename,"r") as file:
                books=file.readlines()
                found=False
                with open(filename,"w") as file:
                    for book in books:
                        try:
                            title,author,price=book.strip().split(',')
                        except ValueError:
                            print("Skipping malfunction line: ",book.strip())
                        if title==title1:
                            print(f'Deleted - {title},{author},{price}')
                            found=True
                        else:
                            file.write(book)
                if not found:
                    print("Book not found.")
        else:
            print("Inventory file does not exist.")    
    except Exception as e:
        print("An error occurred: ",e)
        
def main():
    filename="AI.txt"
    while True:
        display_name()
        choice=input("Enter your choice: ")
        if choice=="1":
            new_book(filename)
        elif choice=="2":
            view_inventory(filename)
        elif choice=="3":
            search_book(filename)
        elif choice=="4":
            delete_book(filename)
            print("Exiting the code.")
            break
        else:
            print("Invalid choice.")

if __name__=="__main__":
    main()


