#import
import random
import string
from prettytable import PrettyTable

#file creation
#students
file=open("students_sorted.txt", "w")
file.close()
#teachers
file=open("teachers_sorted.txt", "w")
file.close()
#substitute teachers
file=open("substitute_teachers_sorted.txt", "w")
file.close()

#functions
#program for exception handling
def eh(input_value):
    try:
        result = int(input_value)
        return True
    except ValueError:
        print("Error: The input value is not a valid integer.")
        return False
    except TypeError:
        print("Error: Invalid input type.")
        return False
    except:
        print("An unexpected error occurred.")
        return False
    
#captcha function
def verify():
    x=str(random.randint(0,9))+random.choice(string.ascii_uppercase)+str(random.randint(0,9))+random.choice(string.ascii_lowercase)+str(random.randint(0,9))+random.choice(string.ascii_uppercase)
    print(x)
    captcha=input("Enter the above code: \n")
    if x==captcha:
        return True
    else:
         return False

#for printing students database
def st1():
    st1= PrettyTable()
    st1.field_names = ["Admission No.", "Name of Student", "Age", "Class", "Gender", "DOB", "DateOfAdmission", "Contact"]
    for adm in students.keys():
        st1.add_row([adm, students[adm]['name'], students[adm]['age'], students[adm]['class'], students[adm]['gender'], students[adm]['DOB'], students[adm]['DateOfAdmission'], students[adm]['Contact']])
    print(st1)

#for printing teachers database
def te1():
    te1= PrettyTable()
    te1.field_names = ["Teachers ID", "Name of Teacher", "DateOfJoining", "Salary", "Age", "Qualifications", "Post", "Contact", "Years Of Service"]
    for adm in teachers.keys():
        te1.add_row([adm, teachers[adm]['name'], teachers[adm]['DateOfJoining'], teachers[adm]['Salary'], teachers[adm]['Age'], teachers[adm]['Qualifications'], teachers[adm]['Post'], teachers[adm]['Contact'], teachers[adm]['YearsOfService']])
    print(te1)

#for printing substitute teachers database
def te2():
    te2= PrettyTable()
    te2.field_names = ["Teachers ID", "Name of Teacher", "DateOfJoining", "Salary", "Age", "Qualifications", "Post", "Contact", "Years Of Contract"]
    for adm in substitute_teachers.keys():
        te2.add_row([adm, substitute_teachers[adm]['name'], substitute_teachers[adm]['DateOfJoining'], substitute_teachers[adm]['Salary'], substitute_teachers[adm]['Age'], substitute_teachers[adm]['Qualifications'], substitute_teachers[adm]['Post'], substitute_teachers[adm]['Contact'], substitute_teachers[adm]['YearsOfContract']])
    print(te2)

#for printing main menu of students
def Students():
    table2 = PrettyTable()
    table2.field_names = ["S. No.", "Tasks"]
    table2.add_row([1, "Print Student"])
    table2.add_row([2, "Add Student"],)
    table2.add_row([3, "Remove Student"])
    table2.add_row([4, "Update Student"])
    table2.add_row([5, "Sort Students"])
    table2.add_row([6, "Exit"])
    print(table2)

#for printing menu for updating students
def u_Students():
    table3 = PrettyTable()
    table3.field_names = ["S. No.", "Tasks"]
    table3.add_row([1, "Update Name"])
    table3.add_row([2, "Update Class"],)
    table3.add_row([3, "Update Age"])
    table3.add_row([4, "Update Contact"])
    table3.add_row([5, "Exit"])
    print(table3)

#for printing sort teachers menu
def s_teachers():
    s_stu=PrettyTable()
    s_stu.field_names = ["S. No.", "Sorting Categories"]
    s_stu.add_row([1, "Sort Alphabetically"])
    s_stu.add_row([2, "Sort by YearOfJoining"])
    s_stu.add_row([3, "Sort by Salary"])
    s_stu.add_row([4, "Sort by Age"])
    s_stu.add_row([5, "Sort by years of service"])
    s_stu.add_row([6, "Exit"])
    print(s_stu)

#for printing menu for updating teachers
def u_Teachers():
    table3 = PrettyTable()
    table3.field_names = ["S. No.", "Tasks"]
    table3.add_row([1, "Update Name"])
    table3.add_row([2, "Update Salary"],)
    table3.add_row([3, "Update Age"])
    table3.add_row([4, "Update Qualifications"])
    table3.add_row([5, "Update Post"])
    table3.add_row([6, "Update Contact"])
    table3.add_row([7, "Exit"])
    print(table3)

#for printing sorting menu for students
def s_students():
    s_stu=PrettyTable()
    s_stu.field_names = ["S. No.", "Sorting Categories"]
    s_stu.add_row([1, "Sort Alphabetically"])
    s_stu.add_row([2, "Sort Age-wise"])
    s_stu.add_row([3, "Sort Class-wise"])
    s_stu.add_row([4, "Sort Gender-wise"])
    s_stu.add_row([5, "Sort by year of admission"])
    s_stu.add_row([6, "Exit"])
    print(s_stu)

#for printing category of sort menu
def age_wise():
    table1=PrettyTable()
    table1.field_names=["S. No.", "        Specify Sort method:        "]
    table1.add_row([1, "Greater than or equal to"])
    table1.add_row([2, "Equal to"])
    table1.add_row([3, "Less than or equal to"])
    table1.add_row([4, "Exit"])
    print(table1)

#for printing main menu after logging in
def main():
    table1=PrettyTable()
    table1.field_names=["S. No.", "Select Database"]
    table1.add_row([1, "Teachers"])
    table1.add_row([2, "Substitute Teachers"])
    table1.add_row([3, "Students"],)
    table1.add_row([4, "Exit"])
    print(table1)

#for printing main menu of teachers and substitute teachers
def Teachers():
    table = PrettyTable()
    table.field_names = ["S. No.", "Tasks"]
    table.add_row([1, "Print Teacher"],)
    table.add_row([2, "Add Teacher"],)
    table.add_row([3, "Remove Teacher"])
    table.add_row([4, "Update Teacher"])
    table.add_row([5, "Sort Teachers"])
    table.add_row([6, "Exit"])
    print(table)

#for printing line
def line():
    for i in range(1,101):
        print("-", end="")
    print()

#for adding gender
def gender():
    gender=PrettyTable()
    gender.field_names = ["S. No.", "Genders"]
    gender.add_row([1, "Male"],)
    gender.add_row([2, "Female"])
    gender.add_row([3, "Others"])
    print(gender)

#dictionaries
#teachers dict
teachers = {
    1: {
        "name": "John Doe",
        "DateOfJoining": "2010-06-15",
        "Salary": 50000,
        "Age": 35,
        "Qualifications": "B.Ed, M.Ed",
        "Post": "Assistant Teacher",
        "Contact": "+91-9876543210",
        "YearsOfService": 13
    },
    2: {
        "name": "Jane Smith",
        "DateOfJoining": "2015-03-12",
        "Salary": 60000,
        "Age": 30,
        "Qualifications": "B.Sc, B.Ed, M.Ed",
        "Post": "Senior Teacher",
        "Contact": "+91-9876543211",
        "YearsOfService": 8
    },
    3: {
        "name": "Bob Johnson",
        "DateOfJoining": "2018-08-01",
        "Salary": 75000,
        "Age": 40,
        "Qualifications": "B.A, B.Ed, M.A, M.Ed",
        "Post": "Head Teacher",
        "Contact": "+91-9876543212",
        "YearsOfService": 5
    },
    4: {
        "name": "Alice Brown",
        "DateOfJoining": "2012-09-20",
        "Salary": 55000,
        "Age": 38,
        "Qualifications": "B.Sc, B.Ed",
        "Post": "Assistant Teacher",
        "Contact": "+91-9876543213",
        "YearsOfService": 11
    },
    5: {
        "name": "David Lee",
        "DateOfJoining": "2017-05-18",
        "Salary": 65000,
        "Age": 32,
        "Qualifications": "B.A, B.Ed, M.A",
        "Post": "Senior Teacher",
        "Contact": "+91-9876543214",
        "YearsOfService": 6
    },
    6: {
        "name": "Amy Wang",
        "DateOfJoining": "2019-02-10",
        "Salary": 70000,
        "Age": 29,
        "Qualifications": "B.Sc, B.Ed, M.Ed",
        "Post": "Senior Teacher",
        "Contact": "+91-9876543215",
        "YearsOfService": 4
    }
}

#substitute teachers dict
substitute_teachers = {
    101: {
        "name": "John Doe",
        "DateOfJoining": "2019-06-19",
        "Salary": 50000,
        "Age": 35,
        "Qualifications": "B.Ed, M.Ed",
        "Post": "Assistant Teacher",
        "Contact": "9876543210",
        "YearsOfContract": 4
    },
    102: {
        "name": "Jane Smith",
        "DateOfJoining": "2022-03-12",
        "Salary": 60000,
        "Age": 30,
        "Qualifications": "B.Sc, B.Ed, M.Ed",
        "Post": "Senior Teacher",
        "Contact": "9876543211",
        "YearsOfContract": 1
    },
    103: {
        "name": "Bob Johnson",
        "DateOfJoining": "2021-08-01",
        "Salary": 75000,
        "Age": 40,
        "Qualifications": "B.A, B.Ed, M.A, M.Ed",
        "Post": "Head Teacher",
        "Contact": "9876543212",
        "YearsOfContract": 2
    },
    104: {
        "name": "Alice Brown",
        "DateOfJoining": "2023-09-20",
        "Salary": 55000,
        "Age": 38,
        "Qualifications": "B.Sc, B.Ed",
        "Post": "Assistant Teacher",
        "Contact": "9876543213",
        "YearsOfContract": 5
    },
    105: {
        "name": "David Lee",
        "DateOfJoining": "2022-05-18",
        "Salary": 65000,
        "Age": 32,
        "Qualifications": "B.A, B.Ed, M.A",
        "Post": "Junior Maths Teacher",
        "Contact": "9876543214",
        "YearsOfContract": 1
    },
    106: {
        "name": "Amy Wang",
        "DateOfJoining": "2019-02-10",
        "Salary": 70000,
        "Age": 29,
        "Qualifications": "B.Sc, B.Ed, M.Ed",
        "Post": "Assistant Teacher",
        "Contact": "+91-9876543215",
        "YearsOfContract": 4
    }
}

#students dict
students = {
    10001:{
        "name": "Lily Garcia",
        "age": 6,
        "class": 1,
        "gender": "Female",
        "DOB": "01/06/2016",
        "DateOfAdmission" : "01/04/2023",
        "Contact": "+91-9876543210"
    },
    10002: {
        "name": "Maya Patel",
        "age": 7,
        "class": 2,
        "gender": "Female",
        "DOB": "14/12/2015",
        "DateOfAdmission" : "01/04/2022",
        "Contact": "+91-9876543211"
    },
    10003: {
        "name": "Sophia Kim",
        "age": 8,
        "class": 3,
        "gender": "Female",
        "DOB": "14/12/2014",
        "DateOfAdmission" : "01/04/2021",
        "Contact": "+91-9876543211"
    },
    10004: {
        "name": "Zoe Nguyen",
        "age": 9,
        "class": 4,
        "gender": "Female",
        "DOB": "14/12/2013",
        "DateOfAdmission" : "01/04/2020",
        "Contact": "+91-9876543211"
    },
    10005: {
        "name": "Isabella Hernandez",
        "age": 10,
        "class": 5,
        "gender": "Female",
        "DOB": "14/12/2012",
        "DateOfAdmission" : "01/04/2019",
        "Contact": "+91-9876543211"
    },
    10006: {
        "name": "Savannah Singh",
        "age": 11,
        "class": 6,
        "gender": "Female",
        "DOB": "14/12/2011",
        "DateOfAdmission" : "01/04/2018",
        "Contact": "+91-9876543211"
    },
    10007: {
        "name": "Mia Chen",
        "age": 12,
        "class": 7,
        "gender": "Female",
        "DOB": "14/12/2010",
        "DateOfAdmission" : "01/04/2017",
        "Contact": "+91-9876543211"
    },
    10008: {
        "name": "Grace Lee",
        "age": 13,
        "class": 8,
        "gender": "Female",
        "DOB": "14/12/2009",
        "DateOfAdmission" : "01/04/2016",
        "Contact": "+91-9876543211"
    },
    10009: {
        "name": "Victoria Rodriguez",
        "age": 14,
        "class": 9,
        "gender": "Female",
        "DOB": "14/12/2008",
        "DateOfAdmission" : "01/04/2015",
        "Contact": "+91-9876543211"
    },
    10010: {
        "name": "Ava Smith",
        "age": 15,
        "class": 10,
        "gender": "Female",
        "DOB": "14/12/2007",
        "DateOfAdmission" : "01/04/2014",
        "Contact": "+91-9876543211"
    },
    10011: {
        "name": "Scarlett Johnson",
        "age": 16,
        "class": 11,
        "gender": "Female",
        "DOB": "14/12/2006",
        "DateOfAdmission" : "01/04/2013",
        "Contact": "+91-9876543211"
    },
    10012: {
        "name": "Audrey Davis",
        "age": 18,
        "class": 12,
        "gender": "Female",
        "DOB": "14/12/2005",
        "DateOfAdmission" : "01/04/2012",
        "Contact": "+91-9876543211"
    },
    10013:{
        "name": "Ethan Patel",
        "age": 6,
        "class": 1,
        "gender": "Male",
        "DOB": "01/06/2016",
        "DateOfAdmission" : "01/04/2023",
        "Contact": "+91-9876543210"
    },
    10014: {
        "name": "Liam Nguyen",
        "age": 7,
        "class": 2,
        "gender": "Male",
        "DOB": "14/12/2015",
        "DateOfAdmission" : "01/04/2022",
        "Contact": "+91-9876543211"
    },
    10015: {
        "name": "Benjamin Kim",
        "age": 8,
        "class": 3,
        "gender": "Male",
        "DOB": "14/12/2014",
        "DateOfAdmission" : "01/04/2021",
        "Contact": "+91-9876543211"
    },
    10016: {
        "name": "Noah Singh",
        "age": 9,
        "class": 4,
        "gender": "Male",
        "DOB": "14/12/2013",
        "DateOfAdmission" : "01/04/2020",
        "Contact": "+91-9876543211"
    },
    10017: {
        "name": "William Lee",
        "age": 10,
        "class": 5,
        "gender": "Male",
        "DOB": "14/12/2012",
        "DateOfAdmission" : "01/04/2019",
        "Contact": "+91-9876543211"
    },
    10018: {
        "name": "Alexander Hernandez",
        "age": 11,
        "class": 6,
        "gender": "Male",
        "DOB": "14/12/2011",
        "DateOfAdmission" : "01/04/2018",
        "Contact": "+91-9876543211"
    },
    10019: {
        "name": "Michael Garcia",
        "age": 12,
        "class": 7,
        "gender": "Male",
        "DOB": "14/12/2010",
        "DateOfAdmission" : "01/04/2017",
        "Contact": "+91-9876543211"
    },
    10020: {
        "name": "James Rodriguez",
        "age": 13,
        "class": 8,
        "gender": "Male",
        "DOB": "14/12/2009",
        "DateOfAdmission" : "01/04/2016",
        "Contact": "+91-9876543211"
    },
    10021: {
        "name": "Daniel Brown",
        "age": 14,
        "class": 9,
        "gender": "Male",
        "DOB": "14/12/2008",
        "DateOfAdmission" : "01/04/2015",
        "Contact": "+91-9876543211"
    },
    10022: {
        "name": "Samuel Davis",
        "age": 15,
        "class": 10,
        "gender": "Female",
        "DOB": "14/12/2007",
        "DateOfAdmission" : "01/04/2014",
        "Contact": "+91-9876543211"
    },
    10023: {
        "name": "Christopher Johnson",
        "age": 16,
        "class": 11,
        "gender": "Male",
        "DOB": "14/12/2006",
        "DateOfAdmission" : "01/04/2013",
        "Contact": "+91-9876543211"
    },
    10024: {
        "name": "Joseph Wilson",
        "age": 18,
        "class": 12,
        "gender": "Male",
        "DOB": "14/12/2005",
        "DateOfAdmission" : "01/04/2012",
        "Contact": "+91-9876543211"
    }
}

#create id
while True:
    line()
    print("MINIMUM REQUIREMENTS FOR ID AND PASSWORD")
    print("ID should have alphabets only \n", "It must contain lowercase alphabets only")
    print("Password must contain alphabets and number. \n", "It must contain minimum 8 characters")
    line()

    #id creation
    id1=input("Create Login ID: ")
    if id1.isalpha()!=True or id1.islower()!=True:
        line()
        print("Sorry, but your ID doesn't quite make the cut. Please spruce it up to meet our requirements.")
        line()
        if id1.isalpha()!=True and id1.islower()!=True:
            print("ID contains special symbols or numbers and special uppercase letters")
            continue
        if id1.isalpha()!=True:
            print("ID contains special symbols or numbers")
            continue
        elif id1.islower()!=True:
            print("ID contains uppercase letters")
            continue
        line()

    #password creation
    passw1=input("Create Password: ")
    if passw1.isalnum()!=True or len(passw1)<=7:
        line()
        print("Uh-oh, looks like your password isn't up to par. Please jazz it up to meet our security standards.")
        line()
        if passw1.isalnum()!=True and len(passw1)<=7:
            print("Password doesn't contains alphabets or numbers and have less than 8 characters")
            continue
        elif passw1.isalnum()!=True:
            print("Password doesn't contains alphabets or numbers")
            continue
        elif len(passw1)<=7:
            print("Password have less than 8 characters")
            continue
        line()

    b=verify()
    line()
    if b!=True:
        print("Wrong Captcha. \n Please Try Again!")
        continue
    
    if passw1.isalnum() and len(passw1)>7 and id1.isalpha() and id1.islower() and b:
        print("ID Created Succesfully")
        break

#login
line()
id=input("Enter Login ID: ")
passw=input("Enter Password: ")
captcha=verify()
line()

if id1==id and passw1==passw and captcha==True:
     #login successful message
     print("Access granted!")

     #main program
     line()
     print("WELCOME TO SCHOOL MANAGEMENT SYSTEM")
     line()
     print("With our user-friendly interface, you'll be able to navigate through mountains of data effortlessly, allowing you to make informed decisions and keep your school running like a well-oiled machine. So come on in and explore the limitless possibilities of our School Database!")
     line()
     
     while True:
         main()
         
         #for choice in main
         ch1=input("Enter Your Choice:")
         if eh(ch1):
             ch1=int(ch1)

         #for exiting from main
         if ch1==4:
             print("You're exiting....")
             print("Thanks for using School Management System!")
             break

         #for teachers
         if ch1==1:
            
             while True:
              Teachers()
              ch2=input("Enter Your Choice:")
              if eh(ch2):
                  ch2=int(ch2)
              #for printing teachers database
              if ch2==1:
                  te1()

              #for adding teachers
              elif ch2==2:
                  #input of new teacher's details
                  t_id=input("Enter New Teacher's ID")
                  if eh(t_id):
                      t_id=int(t_id)
                  t_name=input("Enter New Teacher's Name:")
                  t_DOJ=input("Enter date of joining(YYYY-MM-DD):")
                  t_sal=input("Enter New Teacher's Salary:")
                  if eh(t_sal):
                      t_sal=int(t_sal)
                  t_age=input("Enter New Teacher's Age:")
                  if eh(t_age):
                      t_age=int(t_age)
                  t_qual=input("Enter New Teacher's Qualification:")
                  t_post=input("Enter New Teacher's post:")
                  t_contact="+91-"+input("Enter New Teacher's Contact No. +91")
                  t_yos=input("Enter Years Of Service:")
                  if eh(t_yos):
                      t_yos=int(t_yos)

                  #adding it to dictionary
                  teachers[t_id]={
                      "name" : t_name,
                      "DateOfJoining" : t_DOJ,
                      "Salary" : t_sal,
                      "Age" : t_age,
                      "Qualifications" : t_qual,
                      "Post" : t_post,
                      "Contact" : t_contact,
                      "YearsOfService" : t_yos
                  }

                  #printing database with data of new teacher
                  k=input("Want print of database? \n Y/N: ")
                  if k=="Y":
                      te1()

              #for removing teacher
              elif ch2==3:
                  r_no=input("Enter Teacher's ID to be removed:")
                  if eh(r_no):
                      r_no=int(r_no)
                  if r_no in teachers.keys():
                    print("Teacher with ID ", r_no, " is successfully removed from teachers database")
                    del teachers[r_no]
                  else:
                    print("Teacher with ID ", r_no, " is not in teachers database")

              #for updating teacher
              elif ch2==4:                  
                  
                  while True:
                      u_Teachers()
                      
                      ch8=input("Enter You Choice:")
                      if eh(ch8):
                          ch8=int(ch8)

                     #for exiting update wizard
                      if ch8>=7:
                          print("You're exiting from update wizard...")
                          break
                      
                      #input teacher's id to be updated
                      emp_id=int(input("Enter ID of Teacher to be updated:"))
                      if eh(emp_id):
                          emp_id=int(emp_id)
                      
                      if emp_id in teachers.keys():
                                                   
                          
                          #for updating name
                          if ch8==1:
                              teachers[emp_id]["name"]=input("Enter Updated Name: ")
                              print("Name updated successfully")
                          
                          #for updating salary
                          if ch8==2:
                              k=input("Enter Updated Salary: ")
                              if eh(k):
                                  teachers[emp_id]["Salary"]=int(k)
                              print("Salary updated successfully")
                          
                          #for updating age
                          if ch8==3:
                              k=input("Enter Updated Age: ")
                              if eh(k):
                                  teachers[emp_id]["Age"]=int(k)
                              print("Age updated successfully")
                           
                          #for updating qualifications
                          if ch8==4:
                              teachers[emp_id]["Qualifications"]=input("Enter Updated Qualifications: ")
                              print("Qualifications updated successfully")
                          
                          #for updating post
                          if ch8==5:
                              teachers[emp_id]["Post"]=input("Enter Updated Post: ")
                              print("Post updated successfully")
                          
                          #for updating contact
                          if ch8==6:
                              teachers[emp_id]["Contact"]="91-"+ input("Enter Updated Contact: ")
                              print("Contact updated successfully")
                      
                      else:
                          print("ID not found in database")
                          continue
                      
              #for sorting teacher
              elif ch2==5:
                  s_teachers()
                  ch11=input("Enter Your Choice: ")
                  if eh(ch11):
                      ch11=int(ch11)
                
                  #alphabetical sort
                  if ch11==1:
                     with open("teachers_sorted.txt", "a") as file:
                         te2= PrettyTable()
                         te2.field_names = ["Teachers ID", "Name of Teacher", "DateOfJoining", "Salary", "Age", "Qualifications", "Post", "Contact", "Years Of Contract"]
                         sorted_st= dict(sorted(teachers.items(), key=lambda x: x[1]["name"]))
                         for adm in sorted_st.keys():
                             te2.add_row([adm, teachers[adm]['name'], teachers[adm]['DateOfJoining'], teachers[adm]['Salary'], teachers[adm]['Age'], teachers[adm]['Qualifications'], teachers[adm]['Post'], teachers[adm]['Contact'], teachers[adm]['YearsOfService']])
                         print("Sorted list is produced in text file")
                         i=input("Want sorted list print? \n Y/N:")
                         if i=="Y":
                             print(te2)
                         file.write("Alphabetically sorted list of teachers \n")
                         file.write(str(te2))
                         file.write("\n")
                     file.close()
                  
                  #for DOJ sort
                  elif ch11==2:
                      while True:
                          with open("teachers_sorted.txt", "a") as file:
                              te2= PrettyTable()
                              te2.field_names = ["Teachers ID", "Name of Teacher", "DateOfJoining", "Salary", "Age", "Qualifications", "Post", "Contact", "Years Of Contract"]
                              age_wise()
                              ch12=input("Enter Your Choice: ")
                              if eh(ch12):
                                  ch12=int(ch12)
                              
                              #greater sort
                              if ch12==1:
                                  year=input("Year: ")
                                  if eh(year):
                                      year=int(year)
                                  for adm in teachers.keys():
                                      if int(teachers[adm]["DateOfJoining"][0:4:1])>=year:
                                          te2.add_row([adm, teachers[adm]['name'], teachers[adm]['DateOfJoining'], teachers[adm]['Salary'], teachers[adm]['Age'], teachers[adm]['Qualifications'], teachers[adm]['Post'], teachers[adm]['Contact'], teachers[adm]['YearsOfService']])
                                  print("Sorted list is produced in text file")
                                  i=input("Want sorted list print? \n Y/N:")
                                  if i=="Y":
                                      print(te2)
                                  file.write("Sorted list of teachers \n")
                                  file.write(str(te2))
                                  file.write("\n")
                          
                              #equal sort
                              elif ch12==2:
                                  year=input("Year: ")
                                  if eh(year):
                                      year=int(year)
                                  for adm in teachers.keys():
                                      if int(teachers[adm]["DateOfJoining"][0:4:1])==year:
                                          te2.add_row([adm, teachers[adm]['name'], teachers[adm]['DateOfJoining'], teachers[adm]['Salary'], teachers[adm]['Age'], teachers[adm]['Qualifications'], teachers[adm]['Post'], teachers[adm]['Contact'], teachers[adm]['YearsOfService']])
                                  print("Sorted list is produced in text file")
                                  i=input("Want sorted list print? \n Y/N:")
                                  if i=="Y":
                                      print(te2)
                                  file.write("Sorted list of teachers \n")
                                  file.write(str(te2))
                                  file.write("\n")
                              
                              #lesser sort
                              elif ch12==3:
                                  year=input("Year: ")
                                  if eh(year):
                                      year=int(year)
                                  for adm in teachers.keys():
                                      if int(teachers[adm]["DateOfJoining"][0:4:1])<=year:
                                          te2.add_row([adm, teachers[adm]['name'], teachers[adm]['DateOfJoining'], teachers[adm]['Salary'], teachers[adm]['Age'], teachers[adm]['Qualifications'], teachers[adm]['Post'], teachers[adm]['Contact'], teachers[adm]['YearsOfService']])
                                  print("Sorted list is produced in text file")
                                  i=input("Want sorted list print? \n Y/N:")
                                  if i=="Y":
                                      print(te2)
                                  file.write("Sorted list of teachers \n")
                                  file.write(str(te2))
                                  file.write("\n")

                              else:
                                  print("You're exiting from DateOfJoining-sort")
                                  break
                                          
                          file.close()       
                              
                  #for salary sort
                  elif ch11==3:
                      while True:
                          with open("teachers_sorted.txt", "a") as file:
                              te2= PrettyTable()
                              te2.field_names = ["Teachers ID", "Name of Teacher", "DateOfJoining", "Salary", "Age", "Qualifications", "Post", "Contact", "Years Of Contract"]
                              age_wise()
                              ch12=input("Enter Your Choice: ")
                              if eh(ch12):
                                  ch12=int(ch12)
                              
                              #greater sort
                              if ch12==1:
                                  year=input("Salary: ")
                                  if eh(year):
                                      year=int(year)
                                  for adm in teachers.keys():
                                      if teachers[adm]["Salary"]>=year:
                                          te2.add_row([adm, teachers[adm]['name'], teachers[adm]['DateOfJoining'], teachers[adm]['Salary'], teachers[adm]['Age'], teachers[adm]['Qualifications'], teachers[adm]['Post'], teachers[adm]['Contact'], teachers[adm]['YearsOfService']])
                                  print("Sorted list is produced in text file")
                                  i=input("Want sorted list print? \n Y/N:  ")
                                  if i=="Y":
                                      print(te2)
                                  file.write("Sorted list of teachers \n")
                                  file.write(str(te2))
                                  file.write("\n")
                          
                              #equal sort
                              elif ch12==2:
                                  year=input("Salary: ")
                                  if eh(year):
                                      year=int(year)
                                  for adm in teachers.keys():
                                      if teachers[adm]["Salary"]==year:
                                          te2.add_row([adm, teachers[adm]['name'], teachers[adm]['DateOfJoining'], teachers[adm]['Salary'], teachers[adm]['Age'], teachers[adm]['Qualifications'], teachers[adm]['Post'], teachers[adm]['Contact'], teachers[adm]['YearsOfService']])
                                  print("Sorted list is produced in text file")
                                  i=input("Want sorted list print? \n Y/N:")
                                  if i=="Y":
                                      print(te2)
                                  file.write("Sorted list of teachers \n")
                                  file.write(str(te2))
                                  file.write("\n")
                              
                              #lesser sort
                              elif ch12==3:
                                  year=input("Salary: ")
                                  if eh(year):
                                      year=int(year)
                                  for adm in teachers.keys():
                                      if teachers[adm]["Salary"]<=year:
                                          te2.add_row([adm, teachers[adm]['name'], teachers[adm]['DateOfJoining'], teachers[adm]['Salary'], teachers[adm]['Age'], teachers[adm]['Qualifications'], teachers[adm]['Post'], teachers[adm]['Contact'], teachers[adm]['YearsOfService']])
                                  print("Sorted list is produced in text file")
                                  i=input("Want sorted list print? \n Y/N:")
                                  if i=="Y":
                                      print(te2)
                                  file.write("Sorted list of teachers \n")
                                  file.write(str(te2))
                                  file.write("\n")
                                          
                              else:
                                  print("You're exiting from salary-sort")
                                  break
                          file.close()

                  #for age sort
                  elif ch11==4:
                      while True:
                          with open("teachers_sorted.txt", "a") as file:
                              te2= PrettyTable()
                              te2.field_names = ["Teachers ID", "Name of Teacher", "DateOfJoining", "Salary", "Age", "Qualifications", "Post", "Contact", "Years Of Contract"]
                              age_wise()
                              ch12=input("Enter Your Choice: ")
                              if eh(ch12):
                                ch12=int(ch12)
                              
                              #greater sort
                              if ch12==1:
                                  year=input("Age: ")
                                  if eh(year):
                                      year=int(year)
                                  for adm in teachers.keys():
                                      if teachers[adm]["Age"]>=year:
                                          te2.add_row([adm, teachers[adm]['name'], teachers[adm]['DateOfJoining'], teachers[adm]['Salary'], teachers[adm]['Age'], teachers[adm]['Qualifications'], teachers[adm]['Post'], teachers[adm]['Contact'], teachers[adm]['YearsOfService']])
                                  print("Sorted list is produced in text file")
                                  i=input("Want sorted list print? \n Y/N:")
                                  if i=="Y":
                                      print(te2)
                                  file.write("Sorted list of teachers \n")
                                  file.write(str(te2))
                                  file.write("\n")
                          
                              #equal sort
                              elif ch12==2:
                                  year=input("Age: ")
                                  if eh(year):
                                      year=int(year)
                                  for adm in teachers.keys():
                                      if teachers[adm]["Age"]==year:
                                          te2.add_row([adm, teachers[adm]['name'], teachers[adm]['DateOfJoining'], teachers[adm]['Salary'], teachers[adm]['Age'], teachers[adm]['Qualifications'], teachers[adm]['Post'], teachers[adm]['Contact'], teachers[adm]['YearsOfService']])
                                  print("Sorted list is produced in text file")
                                  i=input("Want sorted list print? \n Y/N:")
                                  if i=="Y":
                                      print(te2)
                                  file.write("Sorted list of teachers \n")
                                  file.write(str(te2))
                                  file.write("\n")
                              
                              #lesser sort
                              elif ch12==3:
                                  year=input("Age: ")
                                  if eh(year):
                                      year=int(year)
                                  for adm in teachers.keys():
                                      if teachers[adm]["Age"]<=year:
                                          te2.add_row([adm, teachers[adm]['name'], teachers[adm]['DateOfJoining'], teachers[adm]['Salary'], teachers[adm]['Age'], teachers[adm]['Qualifications'], teachers[adm]['Post'], teachers[adm]['Contact'], teachers[adm]['YearsOfService']])
                                  print("Sorted list is produced in text file")
                                  i=input("Want sorted list print? \n Y/N:")
                                  if i=="Y":
                                      print(te2)
                                  file.write("Sorted list of teachers \n")
                                  file.write(str(te2))
                                  file.write("\n")
                                          
                              else:
                                  print("You're exiting from age-sort")
                                  break
                          file.close()
                      

                  #for years of service sort
                  elif ch11==5:
                      while True:
                          with open("teachers_sorted.txt", "a") as file:
                              te2= PrettyTable()
                              te2.field_names = ["Teachers ID", "Name of Teacher", "DateOfJoining", "Salary", "Age", "Qualifications", "Post", "Contact", "Years Of Service"]
                              age_wise()
                              ch12=input("Enter Your Choice: ")
                              if eh(ch12):
                                ch12=int(ch12)
                              
                              #greater sort
                              if ch12==1:
                                  year=input("YearsOfService: ")
                                  if eh(year):
                                      year=int(year)
                                  for adm in teachers.keys():
                                      if int(teachers[adm]["YearsOfService"])>=year:
                                          te2.add_row([adm, teachers[adm]['name'], teachers[adm]['DateOfJoining'], teachers[adm]['Salary'], teachers[adm]['Age'], teachers[adm]['Qualifications'], teachers[adm]['Post'], teachers[adm]['Contact'], teachers[adm]['YearsOfService']])
                                  print("Sorted list is produced in text file")
                                  i=input("Want sorted list print? \n Y/N:")
                                  if i=="Y":
                                      print(te2)
                                  file.write("Sorted list of teachers \n")
                                  file.write(str(te2))
                                  file.write("\n")
                          
                              #equal sort
                              elif ch12==2:
                                  year=input("YearsOfService: ")
                                  if eh(year):
                                      year=int(year)
                                  for adm in teachers.keys():
                                      if int(teachers[adm]["YearsOfService"])==year:
                                          te2.add_row([adm, teachers[adm]['name'], teachers[adm]['DateOfJoining'], teachers[adm]['Salary'], teachers[adm]['Age'], teachers[adm]['Qualifications'], teachers[adm]['Post'], teachers[adm]['Contact'], teachers[adm]['YearsOfService']])
                                  print("Sorted list is produced in text file")
                                  i=input("Want sorted list print? \n Y/N:")
                                  if i=="Y":
                                      print(te2)
                                  file.write("Sorted list of teachers \n")
                                  file.write(str(te2))
                                  file.write("\n")
                              
                              #lesser sort
                              elif ch12==3:
                                  year=input("YearsOfService: ")
                                  if eh(year):
                                      year=int(year)
                                  for adm in teachers.keys():
                                      if int(teachers[adm]["YearsOfService"])<=year:
                                          te2.add_row([adm, teachers[adm]['name'], teachers[adm]['DateOfJoining'], teachers[adm]['Salary'], teachers[adm]['Age'], teachers[adm]['Qualifications'], teachers[adm]['Post'], teachers[adm]['Contact'], teachers[adm]['YearsOfService']])
                                  print("Sorted list is produced in text file")
                                  i=input("Want sorted list print? \n Y/N:")
                                  if i=="Y":
                                      print(te2)
                                  file.write("Sorted list of teachers \n")
                                  file.write(str(te2))
                                  file.write("\n")
                                          
                              else:
                                  break
                          file.close()

                  #for exit
                  else:
                      print("You're exiting from sorting wizard...")
                      break

              else:
                  print("You're exiting from School Management System...")
                  break

         #for substitute teachers
         if ch1==2:
             while True:
                 Teachers()
                 ch3=input("Enter Your Choice:")
                 if eh(ch3):
                     ch3=int(ch3)

                 #for printing substitute teachers database
                 if ch3==1:
                     te2()

                 #for adding new subs teacher
                 elif ch3==2:
                     t_id=input("Enter New Teacher's ID")
                     if eh(t_id):
                         t_id=int(t_id)
                     t_name=input("Enter New Teacher's Name:")
                     t_DOJ=input("Enter date of joining(YYYY-MM-DD):")
                     t_sal=input("Enter New Teacher's Salary:")
                     if eh(t_sal):
                         t_id=int(t_sal)
                     t_age=input("Enter New Teacher's Age:")
                     if eh(t_age):
                         t_id=int(t_age)
                     t_qual=input("Enter New Teacher's Qualification:")
                     t_post=input("Enter New Teacher's post:")
                     t_contact="+91-"+input("Enter New Teacher's Contact No. +91-")
                     t_yos=input("Enter Years Of Contract:")
                     if eh(t_yos):
                         t_id=int(t_yos)

                     #adding it to dictionary
                     substitute_teachers[t_id]={
                         "name" : t_name,
                         "DateOfJoining" : t_DOJ,
                         "Salary" : t_sal,
                         "Age" : t_age,
                         "Qualifications" : t_qual,
                         "Post" : t_post,
                         "Contact" : t_contact,
                         "YearsOfContract" : t_yos
                     }

                     #printing database with data of new teacher
                     k=input("Want update printed database? \n Y/N")
                     if k=="Y":
                         te2()

                 #for removing subs teacher from database
                 elif ch3==3:
                     r_no=input("Enter Teacher's ID to be removed:")
                     if eh(r_no):
                         r_no=int(r_no)
                     if r_no in substitute_teachers.keys():
                         print("Teacher with ID ", r_no, " is successfully removed from teachers database")
                         del substitute_teachers[r_no]
                     else:
                         print("Teacher with ID ", r_no, " is not in teachers database")
                     k=input("Want update printed database? \n Y/N:  ")
                     if k=="Y":
                         te2()

                 #for updating subs teacher
                 elif ch3==4:
                     while True:
                         u_Teachers()
                         ch8=input("Enter You Choice:")
                         if eh(ch8):
                             ch8=int(ch8)

                         #for exiting update wizard
                         if ch8>=7:
                             print("You're exiting from update wizard...")
                             break
                         emp_id=input("Enter ID of Teacher to be updated:")
                         if eh(emp_id):
                             emp_id=int(emp_id)
                         if emp_id in substitute_teachers.keys():
                             
                             #for updating name
                             if ch8==1:
                                 substitute_teachers[emp_id]["name"]=input("Enter Updated Name: ")
                                 print("Name updated successfully")
                          
                             #for updating salary
                             if ch8==2:
                                 x=input("Enter Updated Salary: ")
                                 if eh(x):
                                     substitute_teachers[emp_id]["Salary"]=int(x)
                                     print("Salary updated successfully")
                          
                             #for updating age
                             if ch8==3:
                                 x=input("Enter Updated Age: ")
                                 if eh(x):
                                     substitute_teachers[emp_id]["Age"]=int(x)
                                     print("Age updated successfully")
                           
                             #for updating qualifications
                             if ch8==4:
                                 substitute_teachers[emp_id]["Qualifications"]=input("Enter Updated Qualifications: ")
                                 print("Qualifications updated successfully")
                          
                          
                             #for updating post
                             if ch8==5:
                                 substitute_teachers[emp_id]["Post"]=input("Enter Updated Post: ")
                                 print("Post updated successfully")
                          
                          
                             #for updating contact
                             if ch8==6:
                                 substitute_teachers[emp_id]["Contact"]="+91-"+ input("Enter Updated Contact:  +91-")
                                 print("Contact updated successfully")
                      
                         else:
                             print("ID not found in database")
                             continue
                      
                 #for sorting subs teacher
                 elif ch3==5:
                     s_teachers()
                     ch11=input("Enter Your Choice: ")
                     if eh(ch11):
                         ch11=int(ch11)
                
                     #alphabetical sort
                     if ch11==1:
                        with open("substitute_teachers_sorted.txt", "a") as file:
                            te2= PrettyTable()
                            te2.field_names = ["Teachers ID", "Name of Teacher", "DateOfJoining", "Salary", "Age", "Qualifications", "Post", "Contact", "Years Of Contract"]
                            sorted_st= dict(sorted(substitute_teachers.items(), key=lambda x: x[1]["name"]))
                            for adm in sorted_st.keys():
                                te2.add_row([adm, substitute_teachers[adm]['name'], substitute_teachers[adm]['DateOfJoining'], substitute_teachers[adm]['Salary'], teachers[adm]['Age'], teachers[adm]['Qualifications'], substitute_teachers[adm]['Post'], substitute_teachers[adm]['Contact'], substitute_teachers[adm]['YearsOfContract']])
                            print("Sorted list is produced in text file")
                            i=input("Want sorted list print? \n Y/N:")
                            if i=="Y":
                                print(te2)
                            file.write("Alphabetically sorted list of teachers \n")
                            file.write(str(te2))
                            file.write("\n")
                        file.close()
                  
                     #for DOJ sort
                     elif ch11==2:
                         while True:
                             with open("substitute_teachers_sorted.txt", "a") as file:
                                 te2= PrettyTable()
                                 te2.field_names = ["Teachers ID", "Name of Teacher", "DateOfJoining", "Salary", "Age", "Qualifications", "Post", "Contact", "Years Of Contract"]
                                 age_wise()
                                 ch12=input("Enter Your Choice: ")
                                 if eh(ch12):
                                     ch12=int(ch12)
                              
                                 #greater sort
                                 if ch12==1:
                                     year=input("Year: ")
                                     if eh(year):
                                         year=int(year)
                                     for adm in substitute_teachers.keys():
                                         if int(substitute_teachers[adm]["DateofJoining"][0:4:1])>=year:
                                             te2.add_row([adm, substitute_teachers[adm]['name'], substitute_teachers[adm]['DateOfJoining'], substitute_teachers[adm]['Salary'], substitute_teachers[adm]['Age'], substitute_teachers[adm]['Qualifications'], substitute_teachers[adm]['Post'], substitute_teachers[adm]['Contact'], substitute_teachers[adm]['YearsOfContract']])
                                     print("Sorted list is produced in text file")
                                     i=input("Want sorted list print? \n Y/N:")
                                     if i=="Y":
                                         print(te2)
                                     file.write("Sorted list of teachers \n")
                                     file.write(str(te2))
                                     file.write("\n")
                          
                                 #equal sort
                                 elif ch12==2:
                                     year=input("Year: ")
                                     if eh(year):
                                         year=int(year)
                                     for adm in substitute_teachers.keys():
                                         if int(substitute_teachers[adm]["DateofJoining"][0:4:1])==year:
                                             te2.add_row([adm, substitute_teachers[adm]['name'], substitute_teachers[adm]['DateOfJoining'], substitute_teachers[adm]['Salary'], substitute_teachers[adm]['Age'], substitute_teachers[adm]['Qualifications'], substitute_teachers[adm]['Post'], substitute_teachers[adm]['Contact'], substitute_teachers[adm]['YearsOfContract']])
                                     print("Sorted list is produced in text file")
                                     i=input("Want sorted list print? \n Y/N:")
                                     if i=="Y":
                                         print(te2)
                                     file.write("Sorted list of teachers \n")
                                     file.write(str(te2))
                                     file.write("\n")
                              
                                 #lesser sort
                                 elif ch12==3:
                                     year=input("Year: ")
                                     if eh(year):
                                         year=int(year)
                                     for adm in substitute_teachers.keys():
                                         if int(substitute_teachers[adm]["DateofJoining"][0:4:1])<=year:
                                             te2.add_row([adm, substitute_teachers[adm]['name'], substitute_teachers[adm]['DateOfJoining'], substitute_teachers[adm]['Salary'], substitute_teachers[adm]['Age'], substitute_teachers[adm]['Qualifications'], substitute_teachers[adm]['Post'], substitute_teachers[adm]['Contact'], substitute_teachers[adm]['YearsOfContract']])
                                     print("Sorted list is produced in text file")
                                     i=input("Want sorted list print? \n Y/N:")
                                     if i=="Y":
                                         print(te2)
                                     file.write("Sorted list of teachers \n")
                                     file.write(str(te2))
                                     file.write("\n")

                                 else:
                                     break
                                          
                             file.close()  
                 
                
                     #for salary-sort
                     elif ch11==3:
                        while True:
                            with open("substitute_teachers_sorted.txt", "a") as file:
                                te2= PrettyTable()
                                te2.field_names = ["Teachers ID", "Name of Teacher", "DateOfJoining", "Salary", "Age", "Qualifications", "Post", "Contact", "Years Of Contract"]
                                age_wise()
                                ch12=input("Enter Your Choice: ")
                                if eh(ch12):
                                    ch12=int(ch12)
                              
                                #greater sort
                                if ch12==1:
                                    year=input("Salary: ")
                                    if eh(year):
                                        year=int(year)
                                    for adm in substitute_teachers.keys():
                                        if int(substitute_teachers[adm]["Salary"])>=year:
                                            te2.add_row([adm, substitute_teachers[adm]['name'], substitute_teachers[adm]['DateOfJoining'], substitute_teachers[adm]['Salary'], substitute_teachers[adm]['Age'], substitute_teachers[adm]['Qualifications'], substitute_teachers[adm]['Post'], substitute_teachers[adm]['Contact'], substitute_teachers[adm]['YearsOfContract']])
                                    print("Sorted list is produced in text file")
                                    i=input("Want sorted list print? \n Y/N:")
                                    if i=="Y":
                                        print(te2)
                                    file.write("Sorted list of teachers \n")
                                    file.write(str(te2))
                                    file.write("\n")
                          
                                #equal sort
                                elif ch12==2:
                                    year=input("Salary: ")
                                    if eh(year):
                                        year=int(year)
                                    for adm in substitute_teachers.keys():
                                        if int(substitute_teachers[adm]["Salary"])==year:
                                            te2.add_row([adm, substitute_teachers[adm]['name'], substitute_teachers[adm]['DateOfJoining'], substitute_teachers[adm]['Salary'], substitute_teachers[adm]['Age'], substitute_teachers[adm]['Qualifications'], substitute_teachers[adm]['Post'], substitute_teachers[adm]['Contact'], substitute_teachers[adm]['YearsOfContract']])
                                    print("Sorted list is produced in text file")
                                    i=input("Want sorted list print? \n Y/N:")
                                    if i=="Y":
                                        print(te2)
                                    file.write("Sorted list of teachers \n")
                                    file.write(str(te2))
                                    file.write("\n")
                              
                                #lesser sort
                                elif ch12==3:
                                    year=input("Salary: ")
                                    if eh(year):
                                        year=int(year)
                                    for adm in substitute_teachers.keys():
                                        if int(substitute_teachers[adm]["Salary"])<=year:
                                            te2.add_row([adm, substitute_teachers[adm]['name'], substitute_teachers[adm]['DateOfJoining'], substitute_teachers[adm]['Salary'], substitute_teachers[adm]['Age'], substitute_teachers[adm]['Qualifications'], substitute_teachers[adm]['Post'], substitute_teachers[adm]['Contact'], substitute_teachers[adm]['YearsOfContract']])
                                    print("Sorted list is produced in text file")
                                    i=input("Want sorted list print? \n Y/N:")
                                    if i=="Y":
                                        print(te2)
                                    file.write("Sorted list of teachers \n")
                                    file.write(str(te2))
                                    file.write("\n")
                                          
                                else:
                                    break
                        
                            file.close()

                     #for age sort
                     elif ch11==4:
                        while True:
                            with open("substitute_teachers_sorted.txt", "a") as file:
                                te2= PrettyTable()
                                te2.field_names = ["Teachers ID", "Name of Teacher", "DateOfJoining", "Salary", "Age", "Qualifications", "Post", "Contact", "Years Of Contract"]
                                age_wise()
                                ch12=input("Enter Your Choice: ")
                                if eh(ch12):
                                    ch12=int(ch12)
                              
                                #greater sort
                                if ch12==1:
                                    year=input("Age: ")
                                    if eh(year):
                                        year=int(year)
                                    for adm in substitute_teachers.keys():
                                        if substitute_teachers[adm]["Age"]>=year:
                                            te2.add_row([adm, substitute_teachers[adm]['name'], substitute_teachers[adm]['DateOfJoining'], substitute_teachers[adm]['Salary'], substitute_teachers[adm]['Age'], substitute_teachers[adm]['Qualifications'], substitute_teachers[adm]['Post'], substitute_teachers[adm]['Contact'], substitute_teachers[adm]['YearsOfContract']])
                                    print("Sorted list is produced in text file")
                                    i=input("Want sorted list print? \n Y/N:")
                                    if i=="Y":
                                        print(te2)
                                    file.write("Sorted list of teachers \n")
                                    file.write(str(te2))
                                    file.write("\n")
                          
                                #equal sort
                                elif ch12==2:
                                    year=input("Age: ")
                                    if eh(year):
                                        year=int(year)
                                    for adm in substitute_teachers.keys():
                                        if teachers[adm]["Age"]==year:
                                            te2.add_row([adm, teachers[adm]['name'], teachers[adm]['DateOfJoining'], teachers[adm]['Salary'], teachers[adm]['Age'], teachers[adm]['Qualifications'], teachers[adm]['Post'], teachers[adm]['Contact'], teachers[adm]['YearsOfService']])
                                    print("Sorted list is produced in text file")
                                    i=input("Want sorted list print? \n Y/N:")
                                    if i=="Y":
                                        print(te2)
                                    file.write("Sorted list of teachers \n")
                                    file.write(str(te2))
                                    file.write("\n")
                              
                                #lesser sort
                                elif ch12==3:
                                    year=input("Age: ")
                                    if eh(year):
                                        year=int(year)
                                    for adm in teachers.keys():
                                        if teachers[adm]["Age"]<=year:
                                            te2.add_row([adm, teachers[adm]['name'], teachers[adm]['DateOfJoining'], teachers[adm]['Salary'], teachers[adm]['Age'], teachers[adm]['Qualifications'], teachers[adm]['Post'], teachers[adm]['Contact'], teachers[adm]['YearsOfService']])
                                    print("Sorted list is produced in text file")
                                    i=input("Want sorted list print? \n Y/N:")
                                    if i=="Y":
                                        print(te2)
                                    file.write("Sorted list of teachers \n")
                                    file.write(str(te2))
                                    file.write("\n")
                                          
                                else:
                                    print("You're exiting from age-sort")
                                    break
                        
                            file.close()
                      

                     #for years of service sort
                     elif ch11==5:
                        while True:
                            with open("substitute_teachers_sorted.txt", "a") as file:
                                te2= PrettyTable()
                                te2.field_names = ["Teachers ID", "Name of Teacher", "DateOfJoining", "Salary", "Age", "Qualifications", "Post", "Contact", "Years Of Contract"]
                                age_wise()
                                ch12=input("Enter Your Choice: ")
                                if eh(ch12):
                                    ch12=int(ch12)
                              
                                #greater sort
                                if ch12==1:
                                    year=input("YearsOfContract: ")
                                    if eh(year):
                                        year=int(year)
                                    for adm in substitute_teachers.keys():
                                        if int(substitute_teachers[adm]["YearsOfContract"])>=year:
                                            te2.add_row([adm, teachers[adm]['name'], teachers[adm]['DateOfJoining'], teachers[adm]['Salary'], teachers[adm]['Age'], teachers[adm]['Qualifications'], teachers[adm]['Post'], teachers[adm]['Contact'], teachers[adm]['YearsOfContract']])
                                    print("Sorted list is produced in text file")
                                    i=input("Want sorted list print? \n Y/N:")
                                    if i=="Y":
                                        print(te2)
                                    file.write("Sorted list of teachers \n")
                                    file.write(str(te2))
                                    file.write("\n")
                          
                                #equal sort
                                elif ch12==2:
                                    year=input("YearsOfContract: ")
                                    if eh(year):
                                        year=int(year)
                                    for adm in substitute_teachers.keys():
                                        if int(substitute_teachers[adm]["YearsOfContract"])==year:
                                            te2.add_row([adm, substitute_teachers[adm]['name'], substitute_teachers[adm]['DateOfJoining'], substitute_teachers[adm]['Salary'], substitute_teachers[adm]['Age'], substitute_teachers[adm]['Qualifications'], substitute_teachers[adm]['Post'], substitute_teachers[adm]['Contact'], substitute_teachers[adm]['YearsOfContract']])
                                    print("Sorted list is produced in text file")
                                    i=input("Want sorted list print? \n Y/N:")
                                    if i=="Y":
                                        print(te2)
                                    file.write("Sorted list of teachers \n")
                                    file.write(str(te2))
                                    
                                    file.write("\n")
                              
                                #lesser sort
                                elif ch12==3:
                                    year=input("YearsOfContract: ")
                                    if eh(year):
                                        year=int(year)
                                    for adm in substitute_teachers.keys():
                                        if int(substitute_teachers[adm]["YearsOfContract"])<=year:
                                            te2.add_row([adm, substitute_teachers[adm]['name'], substitute_teachers[adm]['DateOfJoining'], substitute_teachers[adm]['Salary'], substitute_teachers[adm]['Age'], substitute_teachers[adm]['Qualifications'], substitute_teachers[adm]['Post'], substitute_teachers[adm]['Contact'], substitute_teachers[adm]['YearsOfContract']])
                                    print("Sorted list is produced in text file")
                                    i=input("Want sorted list print? \n Y/N:")
                                    if i=="Y":
                                        print(te2)
                                    file.write("Sorted list of teachers \n")
                                    file.write(str(te2))
                                    file.write("\n")
                                          
                                else:
                                    break
                        
                            file.close()

                     #for exit
                     else:
                         print("You're exiting from sorting wizard...")
                         break

                 #for exiting
                 else:
                    print("You're exiting from Substitute Teacher Management System...")
                    break
            
    
         #for students
         if ch1==3:
             while True:
                 Students()
                 ch4=input("Enter Your Choice:")
                 if eh(ch4):
                     ch4=int(ch4)

                 #for printing the whole students database
                 if ch4==1:
                     st1()

                 #for adding new students
                 elif ch4==2:
                     #details of new students to be added
                     s_admno=input("Enter Admission no. of New Student:")
                     if eh(s_admno):
                         s_admno=int(s_admno)
                     s_name=input("Enter Name of New Student:")
                     s_age=input("Enter Age:")
                     if eh(s_age):
                         s_age=int(s_age)
                     s_class=input("Enter Class:")
                     if eh(s_class):
                         s_class=int(s_class)
                     gender()
                     s_gender=input("Enter gender:")
                     s_gender=s_gender.title()
                     s_dob=input("Enter DOB: DD/MM/YYYY")
                     s_doa=input("Enter Date Of Admission:")
                     s_contact="+91-"+input("Enter Contact No.")
                  
                     #updated dictionary
                     students[s_admno] = {
                         "name": s_name,
                         "age": s_age,
                         "class": s_class,
                         "gender": s_gender,
                         "DOB": s_dob,
                         "DateOfAdmission" : s_doa,
                         "Contact" : s_contact
                     }
                
                     ch6=input("Print Students List? \n Y/N:" )
                     if ch6=='Y':
                         st1()

                 #for removing old students
                 elif ch4==3:
                     r_no=input("Enter Admission No. of Student to be removed: \n")
                     if eh(r_no):
                         r_no=int(r_no)
                     if r_no in students.keys():
                         print("Student with Admission Number ", r_no, " is successfully removed from students database")
                         del students[r_no]
                     else:
                         print("Student with Admission Number ", r_no, " is not in students database")

                 #for updating existing students
                 elif ch4==4:
                     u_admno=input("Enter Admission No. of student to be update: \n")
                     if eh(u_admno):
                         u_admno = int(u_admno)
                     u_Students()
                     while True:
                         ch5=int(input("Enter your choice:"))
                         if ch5==1:
                             u_name=input("Enter Updated Name of Student:")
                             students[u_admno]["name"]=u_name
                             print("Name updated successfully")
                         elif ch5==2:
                             u_class=input("Enter Updated Class of Student:")
                             if eh(u_class):
                                 u_class =int(u_class)
                             students[u_admno]["class"]=u_class
                             print("Class updated successfully")
                         elif ch5==3:
                             u_age=input("Enter Updated Age of Student:")
                             if eh(u_age):
                                 u_age=int(u_age)
                             students[u_admno]["age"]=u_age
                             print("Age updated successfully")
                         elif ch5==4:
                             u_Contact="+91-"+input("Enter Updated Contact of Student:")
                             students[u_admno]["Contact"]=u_Contact
                             print("Contact updated successfully")
                         else:
                             break
                        
                 #for sorting students
                 elif ch4==5:
                     s_students()
                     ch7=input("Enter Your Choice:")
                     if eh(ch7):
                         ch7=int(ch7)

                     #for sorting students alphabetically
                     if ch7==1:
                         with open("students_sorted.txt", "a") as file:
                             st2= PrettyTable()
                             st2.field_names = ["Admission No.", "Name of Student", "Age", "Class", "Gender", "DOB", "DateOfAdmission", "Contact"]
                             sorted_students= dict(sorted(students.items(), key=lambda x: x[1]["name"]))
                             for adm in sorted_students.keys():
                                 st2.add_row([adm, students[adm]['name'], students[adm]['age'], students[adm]['class'], students[adm]['gender'], students[adm]['DOB'], students[adm]['DateOfAdmission'], students[adm]['Contact']])
                             file.write("Alphabetically sorted list of students \n")
                             file.write(str(st2))
                             file.write("\n")
                         file.close()

                     #for sorting students age_wise
                     elif ch7==2:
                         age_wise()
                         ch8=input("Enter Your Choice:")
                         if eh(ch8):
                             ch8=int(ch8)
                    
                         #for greater or equal age students
                         if ch8==1:
                             file=open("students_sorted.txt", "a")
                             age=input("Enter age:")
                             if eh(age):
                                age=int(age)
                             st2= PrettyTable()
                             st2.field_names = ["Admission No.", "Name of Student", "Age", "Class", "Gender", "DOB", "DateOfAdmission", "Contact"]
                             for adm in students.keys():
                                if students[adm]["age"]>=age:
                                    st2.add_row([adm, students[adm]['name'], students[adm]['age'], students[adm]['class'], students[adm]['gender'], students[adm]['DOB'], students[adm]['DateOfAdmission'], students[adm]['Contact']])
                             file.write("Students of age greater than or equal to " + str(age) + " years.\n")
                             file.write(str(st2))
                             file.write("\n")
                             file.close()
                    
                         #for equal age students
                         elif ch8==2:
                             file=open("students_sorted.txt", "a")
                             age=input("Enter age:")
                             if eh(age):
                                 age=int(age)
                             st2= PrettyTable()
                             st2.field_names = ["Admission No.", "Name of Student", "Age", "Class", "Gender", "DOB", "DateOfAdmission", "Contact"]
                             for adm in students.keys():
                                if students[adm]["age"]==age:
                                    st2.add_row([adm, students[adm]['name'], students[adm]['age'], students[adm]['class'], students[adm]['gender'], students[adm]['DOB'], students[adm]['DateOfAdmission'], students[adm]['Contact']])
                             file.write("Students of age equal to " + str(age) + " years.\n")
                             file.write(str(st2))
                             file.write("\n")
                             file.close()
                    
                         #for less or equal age students
                         elif ch8==3:
                             file=open("students_sorted.txt", "a")
                             age=input("Enter age:")
                             if eh(age):
                                 age=int(age)
                             st2= PrettyTable()
                             st2.field_names = ["Admission No.", "Name of Student", "Age", "Class", "Gender", "DOB", "DateOfAdmission", "Contact"]
                             for adm in students.keys():
                                if students[adm]["age"]<=age:
                                     st2.add_row([adm, students[adm]['name'], students[adm]['age'], students[adm]['class'], students[adm]['gender'], students[adm]['DOB'], students[adm]['DateOfAdmission'], students[adm]['Contact']])
                             file.write("Students of age less than or equal to " + str(age) + " years.\n")
                             file.write(str(st2))
                             file.write("\n")
                             file.close()

                     #for sorting students class_wise
                     elif ch7==3:
                         with open("students_sorted.txt", "a") as file:
                             st2= PrettyTable()
                             st2.field_names = ["Admission No.", "Name of Student", "Age", "Class", "Gender", "DOB", "DateOfAdmission", "Contact"]
                             s_class=input("Enter Class:")
                             if eh(s_class):
                                 s_class=int(s_class)
                             for adm in sorted_students.keys():
                                if students[adm]["class"]==s_class:
                                    st2.add_row([adm, students[adm]['name'], students[adm]['age'], students[adm]['class'], students[adm]['gender'], students[adm]['DOB'], students[adm]['DateOfAdmission'], students[adm]['Contact']])
                             file.write("Class-wise sorted list: \n")
                             file.write(str(st2))
                             file.write("\n")
                         file.close()

                     #for sorting students gender-wise
                     elif ch7==4:
                         with open("students_sorted.txt", "a") as file:
                             st2= PrettyTable()
                             st2.field_names = ["Admission No.", "Name of Student", "Age", "Class", "Gender", "DOB", "DateOfAdmission", "Contact"]
                             gender()
                             s_gender=input("Enter Choice:")
                             if eh(s_gender):
                                s_gender=int(s_gender)
                             for adm in sorted_students.keys():
                                if s_gender==1:
                                    if students[adm]["gender"]=="Male":
                                        st2.add_row([adm, students[adm]['name'], students[adm]['age'], students[adm]['class'], students[adm]['gender'], students[adm]['DOB'], students[adm]['DateOfAdmission'], students[adm]['Contact']])
                                if s_gender==2:
                                    if students[adm]["gender"]=="Female":
                                        st2.add_row([adm, students[adm]['name'], students[adm]['age'], students[adm]['class'], students[adm]['gender'], students[adm]['DOB'], students[adm]['DateOfAdmission'], students[adm]['Contact']])
                                if s_gender==3:
                                    if students[adm]["gender"]=="Others":
                                        st2.add_row([adm, students[adm]['name'], students[adm]['age'], students[adm]['class'], students[adm]['gender'], students[adm]['DOB'], students[adm]['DateOfAdmission'], students[adm]['Contact']])
                                else:
                                    print("Please enter an valid option")
                                    print("You're exiting")
                                    break
                             file.write("Class-wise sorted list: \n")
                             file.write(str(st2))
                             file.write("\n")
                         file.close()

                     #for sorting students year of admission
                     elif ch7==5:
                         with open("students_sorted.txt", "a") as file:
                             st2= PrettyTable()
                             st2.field_names = ["Admission No.", "Name of Student", "Age", "Class", "Gender", "DOB", "DateOfAdmission", "Contact"]
                             s_year=input("Enter Year of Admission:")
                             for adm in sorted_students.keys():
                                if len(s_year)==4:
                                    if students[adm]["DateOfAdmission"][6::1]==s_year:
                                        st2.add_row([adm, students[adm]['name'], students[adm]['age'], students[adm]['class'], students[adm]['gender'], students[adm]['DOB'], students[adm]['DateOfAdmission'], students[adm]['Contact']])
                                else:
                                    print("Please enter an valid option")
                                    print("You're exiting")
                                    break
                             file.write("Year of Admission sorted list: \n")
                             file.write(str(st2))
                             file.write("\n")
                         file.close()

                     #for exiting
                     else:
                         print("You're exiting from sorting wizard")
                         break
            
                 #for exiting
                 elif ch4==6:
                     print("You're exiting from Students Database")
                     break
                 
#wrong captcha
elif captcha==False:
      print("Invalid Captcha")
      print(input("Press Enter To Exit \n"))
      print("Thanks For Using School Management System")

#wrong id and password
elif id1==id or passw1==passw:
     print("Wrong id or password")
     print(input("Press Enter To Exit \n"))
     print("Thanks For Using School Management System")
