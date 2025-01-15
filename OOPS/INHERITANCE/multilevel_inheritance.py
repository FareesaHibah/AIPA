# class NSTI:
#     def __init__(self,inst_name,branch):
#         self.inst_name = inst_name
#         self.branch = branch

# class Trade(NSTI):
#     def __init__(self, inst_name, branch,trade):
#         super().__init__(inst_name, branch)
#         self.trade = trade
        
# class Student(Trade):
#     def __init__(self, inst_name, branch, trade, s_name):
#         super().__init__(inst_name, branch, trade)
#         self.s_name = s_name

#     def disp(self):
#         print(f"""Institute name : {self.inst_name}
# Branch : {self.branch}
# Trade : {self.trade}
# Student name : {self.s_name}""")

# x = Student("NSTI", "Ramanthapur", "AIPA", "Fareesa Hibah")
# x.disp()


class Company:
    def __init__(self, branch):
        self.branch = branch

class Cell(Company):
    def __init__(self, branch, cell):
        super().__init__(branch)
        self.cell = cell

class Manager(Cell):
    def __init__(self, branch, cell, man_name):
        super().__init__(branch, cell)
        self.man_name = man_name

class Employee(Manager):
    def __init__(self, branch, cell, man_name, emp_name):
        super().__init__(branch, cell, man_name)
        self.emp_name = emp_name

    def disp(self):
        print(f"""Company branch : {self.branch}
Cell : {self.cell}
Manager : {self.man_name}
Employee : {self.emp_name}""")
        
x = Employee("Sriharikota", "Research and development", "Ayesha Rida", "Fareesa Hibah")
x.disp()
