# ENCAPSULATION
# class bank_account:

#     def __init__(self,name,balance,pin):
#         self.name = name
#         self._balance = balance
#         self.__pin = pin

#     def add(self,money):
#         if money>0:
#             self._balance+=money
#             print(f"{money} added successfully.")
#         else:
#             print(f"{money} cannot be added.")
    
#     def withdraw(self,money,pin):
#         if  pin==self.__pin and money<=self._balance :
#             self._balance-=money
#             print(f"{money} withdrawed successfully.")
#         else:
#             print(f"Cannot withdraw money.")
    
#     def check(self,pin):
#         if pin==self.__pin :
#             print(f"You have {self._balance} rupees in your account.")
#         else:
#             print(f"Enter correct pin.")
    
# x=bank_account("Fareesa",10000,1234)
# x.add(1000000)
# x.withdraw(1000,1234)
# x.withdraw(2000,1234)
# x.check(1234)
# print(f"Account holder: {x.name}, Balance: {x._balance}")

####################################################################################################################################################

# class universe:
#     def __init__(self):
#         pass

#     def display(self):
#         print("""This program gives a brief information about the celestial objects:- 
# 1. Stars and Stellar Objects
# 2. Planets and Related Objects
# 3. Galaxies and Larger Structures
# 4. Cosmic Phenomena
# 5. Dark Matter and Dark Energy""" )   
#         choice=input("What would you like to know about?")
#         return choice

#     def a(self):
#         print("""There are different types of stars:
# Stars: Massive balls of burning gases emitting light and heat, like our Sun.
# Red Giants: Large, luminous stars in the late stages of their life cycle.
# White Dwarfs: Dense remnants of stars after they have exhausted their nuclear fuel.
# Neutron Stars: Extremely dense stars formed from the collapsed core of a supernova.
# Black Holes: Regions of spacetime with gravitational pull so strong that not even light can escape from them.""")
    
#     def b(self):
#         print("""Planets: Large celestial bodies orbiting stars, such as Earth and Jupiter.
# Dwarf Planets: Smaller planetary bodies, like Pluto, that do not clear their orbital path.
# Exoplanets: Planets outside our solar system, orbiting other stars.
# Moons: Natural satellites that orbit planets, like Earth's Moon.
# Asteroids: Small rocky bodies orbiting the Sun, primarily found in the asteroid belt between Mars and Jupiter.
# Comets: Icy bodies that release gas and dust, forming glowing comas and tails as they approach the Sun.""")

#     def c(self):
#         print("""Galaxies: Massive systems of stars, stellar remnants, interstellar gas, and dark matter bound together by gravity. Examples include the Milky Way and Andromeda.
# Galaxy Clusters: Groups of galaxies held together by gravity, forming some of the largest structures in the universe.
# Nebulae: Clouds of gas and dust where new stars are often born. Examples include the Orion Nebula and the Eagle Nebula.
# Quasars: Extremely luminous and active galactic nuclei powered by supermassive black holes, often found in the early universe.""")

#     def d(self):
#         print("""Supernovae: Explosive deaths of massive stars that can outshine entire galaxies for short periods.
# Pulsars: Rapidly rotating neutron stars emitting beams of electromagnetic radiation.
# Cosmic Microwave Background Radiation: The thermal radiation left over from the Big Bang, providing a snapshot of the early universe.""")

#     def e(self):
#         print("""Dark Matter: A form of matter that does not emit, absorb, or reflect light, making it invisible. It is detectable only through its gravitational effects and is thought to account for most of the matter in the universe.
# Dark Energy: A mysterious form of energy responsible for the accelerated expansion of the universe. Its nature remains one of the biggest unsolved mysteries in cosmology.""")

#     def main(self,choice):
#         if choice=="1":
#             x.a()
#         elif choice=="2":
#             x.b()
#         elif choice=="3":
#             x.c()
#         elif choice=="4":
#             x.d()
#         elif choice=="5":
#             x.e()
#         else:
#             print("Exiting the code!")

# x=universe()
# choice=x.display()
# x.main(choice)

#####################################################################################################################################################

# ABSTRACTION
# from abc import ABC , abstractmethod

# class BllingRecord(ABC):
#     @abstractmethod
#     def get_bill(self):
#         pass

#     @abstractmethod
#     def update_bill(self):
#         pass

# class PatientBilling(BllingRecord):
#     def __init__(self,name,id,bill_amount):
#         self.name=name
#         self.id=id
#         self.bill_amount=bill_amount

#     def get_bill(self):
#         print(f"""Patient's name : {self.name}
# Patient's id : {self.id}
# Billing amount : {self.bill_amount}""")
        
#     def update_bill(self,amount):
#         if amount>0:
#             self.bill_amount+=amount
#             print(f"Billing amount updated by {amount}. New amount is : {self.bill_amount}")
#         else:
#             print("Amount should be positive.")

# x = PatientBilling("Dbhcye",21432,8932784)
# x.get_bill()
# x.update_bill(450000)

###############################################################################################################################################################

# INHERITANCE

# class Employee:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary

#     def disp(self):
#         print(f"""Name of the employee : {self.name}
# Age : {self.age}
# salary : {self.salary}""")
        
# class Manager(Employee):
#     def __init__(self, name, age, salary,department):
#         super().__init__(name, age, salary)
#         self.department=department

#     def disp2(self):
#         super().disp()
#         print(f"Working department : {self.department}")  

# x = Manager("Fareesa",19,1200000,"Space and Research")
# x.disp2()

# class Person:
#     def __init__(self,name):
#         self.name = name

#     def greet(self):
#         print(f"Hello {self.name}! Weolcome to python programming.")

# class Employee:
#     def __init__(self, id):
#         self.id = id

#     def get_id(self):
#         print(f"Employee id : {self.id}")

# class Manager(Person , Employee):
#     def __init__(self, name, id):
#         Person.__init__(self,name)
#         Employee.__init__(self, id)

        




# class Founder:
#     def __init__(self, vision):
#         self.vision = vision
        
# class CEO(Founder):
#     def __init__(self, vision, strategy):
#         super().__init__(vision)
#         self.strategy = strategy
        
# class Manager(CEO):
#     def __init__(self, vision, strategy, targets):
#         super().__init__(vision, strategy)
#         self.targets = targets
    
#     def disp(self):
#         print(f"Vision for the company : {self.vision}")
#         print(f"Strategies to be used : {self.strategy}")
#         print(f"Targets to be achieved : {self.targets}")

# x = Manager("To gain recognition globally", "Consistent approach", "Develop a product")
# x.disp()
 


# import requests
# from bs4 import BeautifulSoup
# url = 'https://aimicrodegree.org/'
# res = requests.get(url)
# print(res)
# soup = BeautifulSoup(res.content,'html.parser')

# title = soup.title.text
# body = soup.body.text

# print(title)
# print(body)



# import re
# text = """
# Wristwatch Band Width







# Up to 9 mm







# 10mm - 19mm







# 20mm - 29mm







# 30mm - 39mm







# 40mm & more








# Watch Features







# Alarm







# Back Light







# Bluetooth







# Calendar







# Camera











# Compass







# Countdown







# Lap Timer







# Multi Face







# Multi Time Zone







# Music Player







# Pedometer







# Shock Resistance







# Solar Powered







# Stop Watch





# See more







# Watch Case Shape







# Round







# Square







# Rectangular







# Oval







# Asymmetrical







# Tonneau








# Watch Case Material







# Brass







# Ceramic







# Copper







# Gold Plated







# Plastic











# Platinum







# Resin







# Rose Gold







# Rubber







# Silver







# Stainless Steel







# Titanium







# White Gold







# Yellow Gold







# Alloy





# See more







# Watch Case Diameter







# Up to 19 mm







# 20 mm - 29 mm







# 30 mm - 39 mm







# 40 mm - 49 mm







# 50 mm & more








# Watch Case Thickness







# Up to 4 mm







# 5 mm - 9 mm







# 10 mm - 14 mm







# 15 mm - 19 mm







# 20 mm & more








# Water Resistance







# Up to 9 m







# 10 m - 29 m







# 30 m - 49 m







# 50 m - 99 m







# 100 m - 199 m







# 200 m & more








# Embellishment Feature







# Crystal







# Diamond







# Gemstone







# Glitter







# Pearl







# Rhinestone







# Stud








# Pay On Delivery







# Eligible for Pay On Delivery








# Discount






# 10% Off or more






# 25% Off or more






# 35% Off or more






# 50% Off or more






# 60% Off or more






# 70% Off or more








# New Arrivals






# Last 30 days






# Last 90 days








# Seller







# VRP Telematics







# Titan Company LTD











# Timehut Retail







# JW BRANDS







# Only-Time







# Brandzstorm India







# Vee Ess Sales Pvt Ltd





# See more







# Availability







# Include Out of Stock



















































#                     Your recently viewed items and featured recommendations      ›    View or edit your browsing history     After viewing product detail pages, look here to find an easy way to navigate back to pages you are interested in.         Your recently viewed items and featured recommendations      ›    View or edit your browsing history     After viewing product detail pages, look here to find an easy way to navigate back to pages you are interested in.




#     Back to top






# Get to Know Us


# About Amazon


# Careers


# Press Releases


# Amazon Science





# Connect with Us


# Facebook


# Twitter


# Instagram





# Make Money with Us


# Sell on Amazon


# Sell under Amazon Accelerator


# Protect and Build Your Brand


# Amazon Global Selling


# Supply to Amazon


# Become an Affiliate


# Fulfilment by Amazon


# Advertise Your Products


# Amazon Pay on Merchants





# Let Us Help You


# Your Account


# Returns Centre


# Recalls and Product Safety Alerts


# 100% Purchase Protection


# Amazon App Download


# Help

















# English



# India






# AbeBooksBooks, art& collectibles
# Amazon Web ServicesScalable CloudComputing Services
# AudibleDownloadAudio Books
# IMDbMovies, TV& Celebrities
 

# ShopbopDesignerFashion Brands

# Amazon BusinessEverything ForYour Business
# Prime Now 2-Hour Deliveryon Everyday Items
# Amazon Prime Music100 million songs, ad-freeOver 15 million podcast episodes



# Conditions of Use & Sale Privacy Notice Interest-Based Ads © 1996-2025, Amazon.com, Inc. or its affiliates"""


# import re
# text = """
# AI Micro Degree | AI Programming Assistant Course















 



































# Home
# About Course

# Program Partners



# FAQs
# Contact
# Login

# Register Now


































# What is AI Programming Assistant Course?

# As technology reshapes industries, the need for skilled professionals in emerging fields like Artificial Intelligence (AI) has become imperative.        



#                                                         The Directorate General of Training (DGT), Ministry of Skill Development and Entrepreneurship (MSDE), in collaboration with Microsoft, presents a pioneering AI course tailored for vocational education students, responding to the swift evolution of job roles fueled by AI adoption across various sectors.

# This comprehensive course spans 1,600 hours over twelve months, encompassing theoretical AI concepts and practical applications through lectures, assignments, virtual project-based learning experience and assessments.

# The course aims to build a workforce capable of pursuing careers in AI and create pathways for students transitioning from vocational education to AI-focused professions.














# Training Locations
# 19





# Students
# 300+





# Hours of training
# 1,600










# Admission Timeline



















# About Course

#         The course aims to build a workforce capable of pursuing careers in AI and create pathways for students transitioning from vocational education to AI-focused professions.

# Supported by DGT and Microsoft, with Edunet Foundation as the implementation partner.

# The admission process is applicable as per government norms. Microsoft and Edunet Foundation has no discretion in the process.




# Quick Links

#  About Course
#  Course Content
#  Program Partners
#  FAQs
#  Contact



# Get In Touch

#  aimicrodegree@edunetfoundation.org









#                                                         Copyright © 2025 Edunet Foundation. All rights reserved."""


# xyz = r'[A-Za-z0-9]+[0-9]'
# match = re.findall(xyz,text)
# print(match)





############################################################################################################################################################3
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
 
def abcd(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
 
    print(f"HTML Content: {soup.prettify()}")  # Print the HTML content for debugging
 
    images = []
    for image in soup.find_all('img', src=True):
        img1 = urljoin(url, image['src'])
        images.append(img1)
 
    print(f'Images are: {images}')
    for image in images:
        print(image)
   
    return images  # Return the list of images
 
def abcd1(images, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f'Directory created: {directory}')
   
    for x, image1 in enumerate(images):
        img1 = requests.get(image1).content
        name = f'image{x+1}.jpeg'
        path = os.path.join(directory, name)
 
        with open(path, 'wb') as file1:
            file1.write(img1)
 
        print(f'Saved image: {path}')
 
if __name__ == "__main__":
    url = "https://redtape.com/collections/footwear"
    images = abcd(url)
    if images:
        abcd1(images, 'Images')