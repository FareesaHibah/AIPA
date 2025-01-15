# Question 1: Create a Specialist class that inherits from two parent classes, Doctor and Surgeon. The Doctor class should have a method diagnose that prints "Diagnosing the patient", and the Surgeon class should have a method operate that prints "Performing surgery". The Specialist class should have a constructor that initializes the specialist's name and specialty, 
# and a method display_info that prints the name and specialty.
class Doctor:
    def diagnose(self):
        print("Diagnosing the patient : ")

class Surgeon:
    def operate(self):
        print("Performing surgery.")

class Specialist(Doctor,Surgeon):
    def __init__(self,name,speciality):
        self.name = name
        self.speciality = speciality

    def disp_info(self):
        print(f"Name : {self.name}, Speciality : {self.speciality}")

name = input("Enter name : ")
speciality = input("Enter the speciality : ")

x = Specialist(name,speciality)
x.disp_info()


# Question 2: Create an OnlineCourse class that inherits from two parent classes, CourseContent and InteractiveTools. The CourseContent class should have a method provide_materials that prints "Providing course materials", and the InteractiveTools class should have a method facilitate_interaction that prints "Facilitating student interaction with tools". The OnlineCourse class should have a constructor that initializes the course name and a method display_info that prints the course name. Additionally, write a method start_course that prints "Starting the course".
# class CourseContent:
#     def provide_materials(self):
#         print("Providing course materials.")

# class InteractiveTools:
#     def facilitate_interaction(self):
#         print("Facilitating student interaction with tools.")

# class OnlineCourse(CourseContent,InteractiveTools):
#     def __init__(self, name):
#         self.name = name

#     def disp_info(self):
#         print(f"Course : {self.name}")

#     def start_course(self):
#         print("Starting the course.")

# name = input("Enter the course name : ")

# x = OnlineCourse(name)
# x.disp_info()
# x.start_course()


# Question 3: Create a Drone class that inherits from two parent classes, FlyingMechanism and Camera. The FlyingMechanism class should have a method fly that prints "Drone is flying", and the Camera class should have a method take_photo that prints "Taking a photo". The Drone class should have a constructor that initializes the drone's model and a method display_info that prints the model. Additionally, write a method perform_actions that calls the methods from both parent classes.
# class FlyingMechanism:
#     def fly(self):
#         print("Drone is flying.")

# class Camera:
#     def take_photo(self):
#         print("Taking a photo.")

# class Drone(FlyingMechanism,Camera):
#     def __init__(self,model):
#         self.model = model
    
#     def disp_info(self):
#         print(f"Drone model : {self.model}")

#     def perform_actions(self):
#         super().fly()
#         super().take_photo()

# model = input("Enter model : ")

# x = Drone(model)
# x.disp_info()

