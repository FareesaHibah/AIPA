# import re
### PATTERN TO FIND ALL THE LETTERS IN LOWERCASE ###
# xyz = r'[a-z]'     
# text = "Believe You Can And You're Halfway There."
# #
# match = re.findall(xyz,text)   
# print(match)


### PATTERN TO FIND ALL THE LETTERS IN UPPERCASE ###
# xyz = r'[A-Z]'     
# text = "Believe You Can And You're Halfway There."
# #
# match = re.findall(xyz,text)   
# print(match)


### PATTERN TO FIND ALL NUMBERS BETWEEN 0-9 ###
# xyz = r'[0-9]'     
# text = "There are 20 students in AI batch 2024."
# #
# match = re.findall(xyz,text)   
# print(match)


### PATTERN TO REMOVE A CERTAIN LETTERS OR NUMBERS ###
# xyz = r'[^aeiou ^ABCKJG^12345679870]'     
# text = "Thereoooo are 20 students in AI batch 2024."
# #
# match = re.findall(xyz,text)   
# print(match)


### PATTERN TO PRINT ONLY SPACES BETWEEN WORDS ###
# xyz = r'\s'     
# text = "Believe You Can And You're Halfway There."
# #
# match = re.findall(xyz,text)   
# print(match)


### PATTERN TO PRINT THE SENTENCE WITHOUT ANY SPACE ###
# xyz = r'\S'     
# text = "Believe You Can And You're Halfway There."
# #
# match = re.findall(xyz,text)   
# print(match)


### PATTERN TO PRINT ALPHA-NUMERIC CHARACTERS ###
# xyz = r'\w'     
# text = "Believe_You_Can_And_You're_Halfway_There."
# #
# match = re.findall(xyz,text)   
# print(match)


### PATTERN TO REMOVE LETTERS, NUMBERS, AND ALPHA-NUMERIC CHARACTERS ###
# xyz = r'\W'     
# text = ": ; Believe,You-Can+And?You're`Halfway(_)There."
# #
# match = re.findall(xyz,text)   
# print(match)


### PATTERN TO FIND A CERTAIN LETTER-WORD ###
# xyz = r'\w{5}'     
# text = "Believe You Can And You're Halfway There."
# #
# match = re.findall(xyz,text)   
# print(match)


### PATTERN TO FIND THE NO.OF TIMES A PARTICULAR THING OCCURS ###
# xyz = r'You'     
# text = "Believe You Can And You Are Halfway There."
# #
# match = re.findall(xyz,text)   
# print(match)


### USING QUANTIFIERS ###
# xyz = r'a{3}'       # xyz = r'a{range}' 
# xyz = r'a+'
# xyz = r'a*'
# xyz = r'a?'
# xyz = r'a?b'
# text = "aa aab aabb aabbcc abc aa bb cc"

# match = re.findall(xyz,text)   
# print(match)

### SEARCH ###
# xyz = r'Fareesa'
# x = "Hello! I'm Fareesa."
# match = re.search(xyz,x)
# if match:
#     print("Match found.")
# else:
#     print("No match found.")


### MATCH ###
# xyz = r'Hello!'
# x = "Hello! I'm Fareesa."
# match = re.match(xyz,x)
# if match:
#     print("Match found.")
# else:
#     print("No match found.")


### SUB PATTERN FOR REPLACEMENT ###
# xyz = r'Fareesa'
# rep = 'Hibah'
# x = "My name is Fareesa."
# z = re.sub(xyz,rep,x)
# print(z)

### SPLITTING THE STRING OF THE PATTERN ###
# xyz = r'\d+'
# x = "d37djkjs453fdhfgdfhgj"
# z = re.split(xyz,x)
# print(z)


#############################################################################################################################################################################
# import re
# mob_no = "+91-9603916523"
# xyz = r'^\+?\d{1,2}[-\s]?\d{10}$'
# if re.match(xyz,mob_no):
#     print("Number is valid.")
# else:
#     print("Invalid number.")

# import re
# x = "Hibahrosary7_!$%&#@gmail.com"
# xyz = r'^[A-Za-z0-9_!$%&#]+@[a-z]+\.[a-z]{1,3}$'
# if re.match(xyz,x):
#     print("Valid email.")
# else:
#     print("Invalid email.")

# import re
# password = "Fareesa7@"
# xyz = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$#%&!])[A-Za-z\d@!$#%&]{5,}'
# if re.match(xyz,password):
#     print("Strong password")
# else:
#     print("Weak password")

