# ask -1 : Build a program with the following structure:

# Class Animal has a method eat() and an attribute species.
# Class Mammal inherits from Animal and adds attributes like has_hair and methods like walk().
# Class Dog inherits from Mammal and adds specific attributes like breed and methods like bark().
# Write a program to create a Dog object and demonstrate all the inherited methods.
# class Animal:
#     def __init__(self, species):
#         self.species = species

#     def eat(self):
#         print(f"{self.species} is eating.")

# class Mammal(Animal):
#     def __init__(self, species, has_hair):
#         super().__init__(species)
#         self.has_hair = has_hair

#     def walk(self):
#         print(f"{self.species} is walking.")

# class Dog(Mammal):
#     def __init__(self, species, has_hair, breed):
#         super().__init__(species, has_hair)
#         self.breed = breed
    
#     def bark(self):
#         print(f"{self.species} is barking.")

#     def disp(self):
#         print(f"Species : {self.species} , Does it have hair : {self.has_hair} , Breed : {self.breed}")

# x = Dog("Vertebrate", "Yes", "Bull Dog")
# x.disp()



# Task-2 : Create a multilevel inheritance:

# Class Vehicle has attributes like brand and model.
# Class Car inherits from Vehicle and adds attributes like number_of_doors and fuel_type.
# Class ElectricCar inherits from Car and adds attributes like battery_capacity and range.
# Write methods to display the details of an ElectricCar.
# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

# class Car(Vehicle):
#     def __init__(self, brand, model, no_of_doors, fuel_type):
#         super().__init__(brand, model)
#         self.no_of_doors = no_of_doors
#         self.fuel_type = fuel_type

# class ElectricCar(Car):
#     def __init__(self, brand, model, no_of_doors, fuel_type, battery_capacity, range):
#         super().__init__(brand, model, no_of_doors, fuel_type)
#         self.battery_capacity = battery_capacity
#         self.range = range

#     def disp(self):
#         print(f"""Brand : {self.brand}
# Model : {self.model}
# Number of doors : {self.no_of_doors}
# Fuel type : {self.fuel_type}
# Battery capacity : {self.battery_capacity}
# Range : {self.range}""")

# x = ElectricCar("Rolls-Royce", "Phantom", 4, "Petrol car", "70 Ah", "12 volt")
# x.disp()

# Task -3 :Design a library management system using multilevel inheritance:

# Class Library has attributes library_name and location.
# Class Book inherits from Library and includes attributes like book_name, author, and ISBN.
# Class Borrower inherits from Book and adds attributes like borrower_name and borrow_date.
# Write a program to manage borrowers and display their borrowed book details, including library information.
# class Library:
#     def __init__(self, library_name, location):
#         self.library_name = library_name
#         self.location = location
    
# class Book(Library):
#     def __init__(self, library_name, location, book_name, author, ISBN):
#         super().__init__(library_name, location)
#         self.book_name = book_name
#         self.author = author
#         self.ISBN = ISBN

# class Borrower(Book):
#     def __init__(self, library_name, location, book_name, author, ISBN, borrower_name, borrow_date):
#         super().__init__(library_name, location, book_name, author, ISBN)
#         self.borrower_name = borrower_name
#         self.borrow_date = borrow_date

#     def disp(self):
#         print(f"""Name of the library : {self.library_name}
# Located in : {self.location}
# Name of the book : {self.book_name}
# Author of the book : {self.author}
# ISBN number : {self.ISBN}
# Name of the borrower : {self.borrower_name}
# Borrowed on : {self.borrow_date}""")

# x = Borrower("State Central Library", "Hyderabad", "Ignited Minds", "APJ Abdul Kalam", 9780143424123, "Fareesa Hibah", "31-12-2024")
# x.disp()
