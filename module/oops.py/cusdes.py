

class Employee:
    #default costructor
    def __init__(self):
        self.name = input("Employee Name :")
        self.salary = float(input("salary :"))
    #parameterized consutructor
    def __init__(self,name,salary):
        self.name = name

        self.salary = salary
    def display_employee(self):
        print("Name = {} salary = {}" .
               format(self.name , self.salary))
e = Employee("Zara" , 8000 )
e.display_employee() 