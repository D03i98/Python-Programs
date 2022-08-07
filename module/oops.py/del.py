


class Student:
    def __init__(self,name,mob,email):
        self.name = name
        self.mobile = mob
        self.emailid = email

    # destructor
    def __del__(self):
        print("Delating student " + self.name)

    def display(self):
        print("Name = {}\nMobile = {}\nEmail = {}" . 
               format(self.name ,self.mobile,self.emailid))

s = Student('Priyansh',7754101903 ,'priyansh@gmail.com')
s.display()
del s