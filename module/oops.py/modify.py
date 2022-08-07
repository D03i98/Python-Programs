


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

    def __str__(self):
        return self.name
    def modify_details(self ,name, mob, email):
        self.name = name
        self.mobile = mob
        self.emailid = email

Student_list = []
def display_Student():
    global Student_list
    for i in range(len(Student_list)):
        print(i+1, "." , Student_list[i])
while True:
    print("""Make a choice :
 1. Add Student
 2. Modify Student
 3. Delete Student
 4. View All Students
 5. Quit""")
    ch = int(input("Enter Choice"))
    if ch == 1:
       s = Student(input("eEnter Name :"),
                    input("Enter Mobile :") ,
                    input("Enter Email :"))
       Student_list.append(s)        
    elif ch==2:
            display_Student()
            idx = int(input("Enter number to modify :")) -1
            c1 = input("Do you wish to modify Name : (y/n)")
            if c1.lower() == 'y' :
                name=input("Enter new name :")
            else:
                name = Student_list[idx].name
            c1 = input("Do you wish to modify mobile : (y/n)")
            if c1.lower() == 'y' :
                mob=input("Enter new mobile :")
            else:
                mob = Student_list[idx].mobile
            c1 = input("Do you wish to modify email : (y/n)")
            if c1.lower() == 'y' :
                email=input("Enter new Email :")
            else:
                email = Student_list[idx].emailid    
            Student_list[idx].modify_details(name,mob,email)
    elif ch==3:
            display_Student()
            idx = int (input("Enter number to modify :"))-1
            del Student_list[idx]
            #student_list.pop(idx)
    elif ch==4:
            for student in Student_list:
                student.display()
    elif ch==5:
            break
    else:
            print("Invalid Input")