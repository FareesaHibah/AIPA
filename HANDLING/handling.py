# file =open ("shailesh.txt","r")
# content=file.read()
# print(content)
# file.close()

# with open("shailesh.txt","r") as file:
#     content=file.read()
#     print(content)

# with open ("shailesh.txt","r") as file :
#     for line in file:
#         print(line.strip())


# with open ("shailesh.txt","r") as file:
#     file.readline(23)
#     content=file.read(15)
#     print(content)

# with open("shailesh.txt","w") as file:
#     file.write("Hello , My name is Deepak ")

# with open ("shailesh.txt","a") as file:
#     file.write("\n This is another new line .")


# with open("shailesh.txt","r") as file:
#     # file.read(10)
#     # file.read(5)
#     file.seek(10)
#     print(file.read())
#     print(file.tell())

# try:
#     with open ("shesh.txt","r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File is not available")
# finally:
#     print("Code executed ")

# import os
# file_path="S:/Classroom/Python/xyz.txt"
# if os.path.exists(file_path):
#     os.unlink(file_path)
#     print("File is deleted")
# else:
#     print("file not found")


# import datetime

# def log_message(message):
#     # Open the log file in append mode
#     with open("logfile.txt", "a") as logfile:
#         # Get the current timestamp
#         timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         # Write the timestamp and log message to the file
#         logfile.write(f"{timestamp} - {message}\n")

# if __name__ == "__main__":
#     while True:
#         # Get the log message from the user
#         user_message = input("Enter a log message (or 'exit' to quit): ")
#         if user_message.lower() == "exit":
#             break
#         log_message(user_message)
#         print("Log message appended successfully.")


import os

def menu():
    print("NSTI Book Store ")
    print("1. Add a book:")
    print("2. View books: ")
    print("3. Search for book :")
    print("4. Delete the book ")
    print("5. Exit")

#Add a new book 

def add_new_book(filename):
    try:
        with open(filename,"a") as file:
            title=input("Enter the book title: ")
            author=input("Enter the author:")
            price=input("Enter the price: ")
            book=f'{title},{author},{price}\n'
            file.write(book)
            print("Book added successfully.")
    except Exception as e:
        print(f'An Error Occurred: {e}')

def view_inventory(filename):
    try:
        if os.path.exists(filename):
            with open(filename, "r") as file:
                books = file.readlines()
                if books:
                    print("Inventory:")
                    for book in books:
                        title, author, price = book.strip().split(',')
                        print(f"Title: {title}, Author: {author}, Price: {price}")
                else:
                    print("The inventory is empty.")
        else:
            print("Inventory file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def search_book(filename):
    try:
        if os.path.exists(filename):
            search=input("Enter the book name:")
            with open(filename,"r") as file:
                books=file.readlines()
                found=False
                for book in books:
                    title,author,price=book.strip().split(',')
                    if title==search:
                        print("book Found below:")
                        print(f"Title-{title}")
                        print(f"Author- {author}")
                        print(f"Price-{price}")
                        found=True
                        break
                if not found:
                     print("Book not found.")
        else:
            print("Inventry file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def del_book(filename):
    try:
        if os.path.exists(filename):
            title1=input("Enter the title of book: ").lower()
            with open (filename,"r") as file:
                books=file.readlines()
                found=False
                with open(filename,"w") as file:
                    for book in books:
                        title,author,price=book.strip().split(',')
                        if title==title1:
                          print(f"Deleted -{title},{author},{price}")
                          found=True
                        else:
                            file.write(book) 
                if not found:
                        print("Book not found.") 
        else:
            print("Inventry file does not exists.")
    except Exception as e:
        print(f"An error occurred. {e}")

def main():
    filename="Shailesh.txt"
    while True:
        menu()
        choice=input("Enter you choice : ")
        if choice =="1":
            add_new_book(filename)
        elif choice=="2":
            view_inventory(filename)
        elif choice=="3":
            search_book(filename)
        elif choice=="4":
            del_book(filename)

            print("Exiting the code:")
            break
        else:
            print("Invalid choice .")


if __name__=="__main__":
    main()       

                
                        





