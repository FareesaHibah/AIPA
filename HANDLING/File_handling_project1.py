import os

def display():
    print("Welcome to the Library!")
    print("1. Add a new book")
    print("2. Search for a book")
    print("3. View books")
    print("4. Delete a book")
    print("5. Borrow a book")
    print("6. Return a book")
    print("7. Exit")

def add_book(filename):
    try:
        with open (filename,"a") as file:
            title=input("Enter the title of the book: ")
            author=input("Enter the author name: ")
            year=input("Enter the publication year: ")
            book=f'{title},{author},{year}\n'
            file.write(book)
            print("Book added successfully!")
    except Exception as e:
        print("An error occurred: ",e)

def view(filename):
    try:
        if os.path.exists(filename):
            with open(filename,"r") as file:
                books=file.readlines()
                if books:
                    print("Inventory: ")
                    for book in books:
                        try:
                            title,author,year=book.strip().split(",")
                            print(f'Title: {title}, Author is: {author}, Publication year: {year}\n')
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
            search=input("Enter the name of the book: ")
            with open(filename,"r") as file:
                books=file.readlines()
                found=False
                for book in books:
                    title,author,year=book.strip().split(',')
                    if title==search:
                        print("Book found :")
                        print(f"Title -{title}")
                        print(f"Author - {author}")
                        print(f"Publication year -{year}")
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
            title1=input("Enter the book you want to delete: ").lower()
            with open (filename,"r") as file:
                books=file.readlines()
                found=False
                with open(filename,"w") as file:
                    for book in books:
                        title,author,year=book.strip().split(',')
                        if title==title1:
                          print(f"Deleted - {title}, Author is: {author}, Publication year: {year}")
                          found=True
                        else:
                            file.write(book) 
                if not found:
                        print("Book not found.") 
        else:
            print("Invenotry file does not exist.")
    except Exception as e:
        print(f"An error occurred. {e}")

def borrow(filename,bfilename):
    try:
        if os.path.exists(filename):
            title2=input("Enter the book you want to borrow: ").lower()
            with open (filename,"r") as file:
                books=file.readlines()
                found=False
                with open(filename,"w") as file:
                    for book in books:
                        title,author,year=book.strip().split(',')
                        if title2==title:
                            with open(bfilename,"a") as bfile:
                                bfile.write(book)
                                print(f'Borrowed book: {title}, Author: {author}, Publication year: {year}')
                                found=True
                        else:
                            file.write(book)
                if not found:
                    print("Book not found.")
        else:
            print("Inventory file does not exist.")
    except Exception as e:
        print("An error occurred: ",e)

def return_book(filename,bfilename):
    try:
        if os.path.exists(bfilename):
            title3=input("Enter the book you want to return: ").lower()
            with open(bfilename,"r") as bfile:
                books=bfile.readlines()
                found=False
                with open(bfilename,"w") as file:
                    for book in books:
                        title,author,year=book.strip().split(',')
                        if title3==title:
                            with open(filename,"a") as bfile:
                                bfile.write(book)
                                print(f'Returned book: {title}, Author is: {author}, Publication year: {year}')
                                found=True
                        else:
                            file.write(book)
                if not found:
                    print("Book not found.")
        else:
            print("Inventory file not found.")
    except Exception as e:
        print("An error occurred: ",e)


def main():
    filename="books.txt"
    bfilename="borrowed_books.txt"
    while True:
        display()
        choice=input("Enter your choice : ")
        if choice=="1":
            add_book(filename)
        elif choice=="2":
           search_book(filename)
        elif choice=="3":
            view(filename)
        elif choice=="4":
            del_book(filename)
        elif choice=="5":
            borrow(filename,bfilename)
        elif choice=="6":
            return_book(filename,bfilename)
        elif choice=="7":
            print("Thankyou for visiting the library.")
            break
        else:
            print("Invalid choice.")


if __name__=="__main__":
    main()       

                
