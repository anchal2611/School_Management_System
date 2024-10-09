#import
import random
import string
from prettytable import PrettyTable
from datetime import datetime

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
#salary slip
def generate_salary_slip(teacher_name, teacher_id, basic_salary, allowance, file_name, teacher_post, teacher_doj):
            # Calculate the gross salary
            gross_salary = basic_salary + allowance

            # Calculate the deductions
            tax = 0.1 * basic_salary
            insurance = 0.05 * basic_salary
            deductions = tax + insurance

            # Calculate the net salary
            net_salary = gross_salary - deductions

            # Get current date and time
            current_datetime = datetime.now()

            # Extract the date and time components
            current_date = current_datetime.date()
            current_time = current_datetime.time()

            # Create the salary slip content
            salary_slip_content = "------------------------------\n"
            salary_slip_content += "      SCHOOL TEACHER SALARY SLIP      \n"
            salary_slip_content += "------------------------------\n"
            salary_slip_content += "Teacher Name: {}\n".format(teacher_name)
            salary_slip_content += "Teacher ID: {}\n".format(teacher_id)
            salary_slip_content += "Teacher Post: {}\n".format(teacher_post)
            salary_slip_content += "Teacher DOJ: {}\n".format(teacher_doj)
            salary_slip_content += "Date of salary slip generation: {}\n".format(current_date)
            salary_slip_content += "Date of salary slip generation: {}\n".format(current_time)
            salary_slip_content += "------------------------------\n"
            salary_slip_content += "Earnings:\n"
            salary_slip_content += "Basic Salary: $ {}\n".format(basic_salary)
            salary_slip_content += "Allowance: $ {}\n".format(allowance)
            salary_slip_content += "Gross Salary: $ {}\n".format(gross_salary)
            salary_slip_content += "------------------------------\n"
            salary_slip_content += "Deductions:\n"
            salary_slip_content += "Tax: $ {}\n".format(tax)
            salary_slip_content += "Insurance: $ {}\n".format(insurance)
            salary_slip_content += "Total Deductions: $ {}\n".format(deductions)
            salary_slip_content += "------------------------------\n"
            salary_slip_content += "Net Salary: $ {}\n".format(net_salary)
            salary_slip_content += "------------------------------\n"

            # Save the salary slip to a text file
            with open(file_name, 'w') as file:
                file.write(salary_slip_content)
            file.close()
            print("Salary slip saved to", file_name)

#report_card
def info():
    print("Welcome to the report card generator")
    print("Instructions:")
    print("1. Please enter the asked information correctly.")
    print("2. Report card will be generated in separate text file.")
    print("3. If the value will not follow data type the program will re run")

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
    
#fees payment
def pay_amount(amount):
    # Simulating payment process
    print("Payment process:")
    print("Entered Amount:", amount)
    print("Payment Methods:")
    print("1. UPI")
    print("2. Net Banking")
    print("3. Credit Card")
    print("4. Debit Card")
    payment = float(input("Enter payment amount: "))
    if payment == p:
        payment_method = input("Enter payment method: ")
        if payment_method == "1" or payment_method == "2" or payment_method == "3" or payment_method == "4":
            print("Payment successful!")
            return True
        else:
            print("Wrong Payment Menthod")
            return False
    else:
        print("Payment is not sufficient.")


    # Process payment logic here
    # You can add your specific payment processing code in this section
    # For this example, let's assume the payment is successful
    
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
    te21= PrettyTable()
    te21.field_names = ["Teachers ID", "Name of Teacher", "DateOfJoining", "Salary", "Age", "Qualifications", "Post", "Contact", "Years Of Contract"]
    for adm in substitute_teachers.keys():
        te21.add_row([adm, substitute_teachers[adm]['name'], substitute_teachers[adm]['DateOfJoining'], substitute_teachers[adm]['Salary'], substitute_teachers[adm]['Age'], substitute_teachers[adm]['Qualifications'], substitute_teachers[adm]['Post'], substitute_teachers[adm]['Contact'], substitute_teachers[adm]['YearsOfContract']])
    print(te21)

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

#for checking password
def p1(passw1):
    if passw1.isalnum()!=True or len(passw1)<=7:
        line()
        print("Uh-oh, looks like your password isn't up to par. Please jazz it up to meet our security standards.")
        line()
    if passw1.isalnum()!=True and len(passw1)<=7:
        print("Password doesn't contains alphabets or numbers and have less than 8 characters.")
    elif passw1.isalnum()!=True:
        print("Password doesn't contains alphabets or numbers.")
    elif len(passw1)<=7:
        print("Password have less than 8 characters.")

#for adding gender
def gender():
    gender=PrettyTable()
    gender.field_names = ["S. No.", "Genders"]
    gender.add_row([1, "Male"],)
    gender.add_row([2, "Female"])
    gender.add_row([3, "Others"])
    print(gender)

#for start menu
def start():
    table = PrettyTable()
    table.field_names = ["S. No.", "Tasks"]
    table.add_row([1, "Create ID"],)
    table.add_row([2, "Login"],)
    table.add_row([3, "Update ID's password"])
    table.add_row([4, "Delete ID"])
    table.add_row([5, "Make Report Card"],)
    table.add_row([6, "Make Salary Slip"],)
    table.add_row([7, "Fee Payment"])
    table.add_row([8, "Exit"])
    print(table)

def fees():
    table = PrettyTable()
    table.field_names = ["S. No.", "Tasks"]
    table.add_row([1, "Pay Fees"],)
    table.add_row([2, "Generate Fee Receipt"],)
    table.add_row([3, "Exit"])
    print(table)

#fee receipt
def generate_fee_receipt(student_id, p):
    student = students.get(student_id)
    if student:
        receipt = f"Fee Receipt\n\n"
        receipt += f"Student ID: {student_id}\n"
        receipt += f"Name: {student['name']}\n"
        receipt += f"Age: {student['age']}\n"
        receipt += f"Class: {student['class']}\n"
        receipt += f"Gender: {student['gender']}\n"
        receipt += f"Date of Birth: {student['DOB']}\n"
        receipt += f"Date of Admission: {student['DateOfAdmission']}\n"
        receipt += f"Contact: {student['Contact']}\n\n"
        receipt += "Fee Details:\n"
        # Add fee details here, such as tuition fee, transportation fee, etc.

        # Calculate total fee
        total_fee = p
        # Add fee calculation logic here

        receipt += f"Total Fee: {total_fee}\n"
        receipt += "Payment Information:\n"
        # Add payment details here, such as payment method, transaction ID, etc.

        # Save receipt to a text file
        filename = f"fee_receipt_{student_id}.txt"
        with open(filename, "w") as file:
            file.write(receipt)

        print(f"Fee receipt generated and saved as {filename}")
    else:
        print("Invalid student ID.")

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

#login info
login={
    "anchal":"12345678"
}

while True:
    start()
    line()
    ch1=input("Enter Your Choice: ")
    if eh(ch1):
        ch1=int(ch1)
        line()
        
        #create id
        if ch1==1:
            
            while True:
                line()
                print("MINIMUM REQUIREMENTS FOR ID AND PASSWORD")
                print("ID should have alphabets only \n", "It must contain lowercase alphabets only")
                print("Password must contain alphabets and number. \n", "It must contain minimum 8 characters")
                line()

                line()
                #id creation
                id1=input("Create Login ID: ")
                line()
                if id1.isalpha()!=True or id1.islower()!=True:
                    print("Sorry, but your ID doesn't quite make the cut. Please spruce it up to meet our requirements.")
                    line()
                elif id1.isalpha()!=True and id1.islower()!=True:
                    print("ID contains special symbols or numbers and special uppercase letters.")
                    line()
                    continue
                elif id1.isalpha()!=True:
                    print("ID contains special symbols or numbers.")
                    line()
                    continue
                elif id1.islower()!=True:
                    print("ID contains uppercase letters.")
                    line()
                    continue
                else:
                    if id1 in login.keys():
                        print("ID already exists.")
                        line()
                        break
                    else:
                        print("ID created successfully")
                        line()

                        #password creation
                        passw1=input("Create Password: ")
                        p1(passw1)
                        
                        
                        line()

                        while True:
                            b=verify()
                            line()
                            if b!=True:
                                print("Wrong Captcha. \nPlease Try Again!")
                                continue
                            else:
                                break
    
                        if passw1.isalnum() and len(passw1)>7 and id1.isalpha() and id1.islower() and b:
                            login[id1]=passw1
                            print("You can login now.")
                            break

        #for accessing database
        elif ch1==2:
            #login
            line()
            id_l=input("Enter Login ID: ")
            passw=input("Enter Password: ")
            captcha=verify()
            line()

            id_check=False

            if id_l in login.keys():
                if login[id_l]==passw:
                    id_check=True

            if id_check and captcha==True:
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
                        elif ch1==1:

                            while True:
                                line()
                                Teachers()
                                line()
                            
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
                                        else:
                                            print("Last attempt to enter valid New Teacher's ID")
                                            t_id=input("Enter New Teacher's ID")
                                            if eh(t_id)==False:
                                                print("You're exiting...")
                                                break
                                        t_name=input("Enter New Teacher's Name:")
                                        t_DOJ=input("Enter date of joining(YYYY-MM-DD):")
                                        t_sal=input("Enter New Teacher's Salary:")
                                        if eh(t_sal):
                                            t_sal=int(t_sal)
                                        else:
                                            print("Last attempt to enter valid New Teacher's Salary")
                                            t_sal=input("Enter New Teacher's Salary")
                                            if eh(t_sal)==False:
                                                print("You're exiting...")
                                                break
                                        t_age=input("Enter New Teacher's Age:")
                                        if eh(t_age):
                                            t_age=int(t_age)
                                        else:
                                            print("Last attempt to enter valid New Teacher's Age")
                                            t_age=input("Enter New Teacher's Age")
                                            if eh(t_age)==False:
                                                print("You're exiting...")
                                                break
                                        t_qual=input("Enter New Teacher's Qualification:")
                                        t_post=input("Enter New Teacher's post:")
                                        t_contact="+91-"+input("Enter New Teacher's Contact No. +91")
                                        t_yos=input("Enter Years Of Service:")
                                        if eh(t_yos):
                                            t_yos=int(t_yos)
                                        else:
                                            print("Last attempt to enter valid New Teacher's Years of Service")
                                            t_yos=input("Enter New Teacher's Years of Service")
                                            if eh(t_yos)==False:
                                                print("You're exiting...")
                                                break

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
                                                emp_id=input("Enter ID of Teacher to be updated:")
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
                      
                                                        #id not found
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
                                                                        if int(teachers[adm]["YearsOfService"])>=year:
                                                                            te2.add_row([adm, teachers[adm]['name'], teachers[adm]['DateOfJoining'], teachers[adm]['Salary'], teachers[adm]['Age'], teachers[adm]['Qualifications'], teachers[adm]['Post'], teachers[adm]['Contact'], teachers[adm]['YearsOfService']])
                                                                    print("Sorted list is produced in text file")
                                                                    i=input("Want sorted list print? \n Y/N:")
                                                                    if i=="Y":
                                                                        print(te2)
                                                                    file.write("Sorted list of teachers \n")
                                                                    file.write(str(te2))
                                                                    file.write("\n")
                                          
                                                            else:
                                                                print("You're exiting Years of service sort...")
                                                                break
                                        
                                                    file.close()

                                            #for exit
                                            else:
                                                print("You're exiting from sorting wizard...")
                                                break

                                    #exiting teacher's databasr
                                    else:
                                        print("You're exiting from Teachers Management System...")
                                        break

                        #for substitute teachers
                        elif ch1==2:
                            while True:
                                line()
                                Teachers()
                                line()

                                ch3=input("Enter Your Choice:")
                                if eh(ch3):
                                    ch3=int(ch3)

                                    #for printing substitute teachers database
                                    if ch3==1:
                                        line()
                                        te2()
                                        line()

                                    #for adding new subs teacher
                                    elif ch3==2:
                                        #input of new teacher's details
                                        line()
                                        t_id=input("Enter New Teacher's ID")
                                        if eh(t_id):
                                            t_id=int(t_id)
                                        else:
                                            print("Last attempt to enter valid New Teacher's ID")
                                            t_id=input("Enter New Teacher's ID")
                                            if eh(t_id)==False:
                                                print("You're exiting...")
                                                break
                                        t_name=input("Enter New Teacher's Name:")
                                        t_DOJ=input("Enter date of joining(YYYY-MM-DD):")
                                        t_sal=input("Enter New Teacher's Salary:")
                                        if eh(t_sal):
                                            t_sal=int(t_sal)
                                        else:
                                            print("Last attempt to enter valid New Teacher's Salary")
                                            t_sal=input("Enter New Teacher's Salary")
                                            if eh(t_sal)==False:
                                                print("You're exiting...")
                                                break
                                        t_age=input("Enter New Teacher's Age:")
                                        if eh(t_age):
                                            t_age=int(t_age)
                                        else:
                                            print("Last attempt to enter valid New Teacher's Age")
                                            t_age=input("Enter New Teacher's Age")
                                            if eh(t_age)==False:
                                                print("You're exiting...")
                                                break
                                        t_qual=input("Enter New Teacher's Qualification:")
                                        t_post=input("Enter New Teacher's post:")
                                        t_contact="+91-"+input("Enter New Teacher's Contact No. +91")
                                        t_yos=input("Enter Years Of Service:")
                                        if eh(t_yos):
                                            t_yos=int(t_yos)
                                        else:
                                            print("Last attempt to enter valid New Teacher's Years of Service")
                                            t_yos=input("Enter New Teacher's Years of Service")
                                            if eh(t_yos)==False:
                                                print("You're exiting...")
                                                break

                                        line()

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
                                        k=input("Want update printed database? \nY/N")
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
                                                k=input("Want update printed database? \nY/N:  ")
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
                                                        elif ch8==2:
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
                                                        te2.add_row([adm, substitute_teachers[adm]['name'], substitute_teachers[adm]['DateOfJoining'], substitute_teachers[adm]['Salary'], substitute_teachers[adm]['Age'], substitute_teachers[adm]['Qualifications'], substitute_teachers[adm]['Post'], substitute_teachers[adm]['Contact'], substitute_teachers[adm]['YearsOfContract']])
                                                    
                                                    print("Sorted list is produced in text file")
                                                    i=input("Want sorted list print? \nY/N:")
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
                                                                    if int(substitute_teachers[adm]["DateOfJoining"][0:4:1])>=year:
                                                                        te2.add_row([adm, substitute_teachers[adm]['name'], substitute_teachers[adm]['DateOfJoining'], substitute_teachers[adm]['Salary'], substitute_teachers[adm]['Age'], substitute_teachers[adm]['Qualifications'], substitute_teachers[adm]['Post'], substitute_teachers[adm]['Contact'], substitute_teachers[adm]['YearsOfContract']])
                                                                
                                                                print("Sorted list is produced in text file")
                                                                i=input("Want sorted list print? \nY/N:")
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
                                                                    if int(substitute_teachers[adm]["DateOfJoining"][0:4:1])==year:
                                                                        te2.add_row([adm, substitute_teachers[adm]['name'], substitute_teachers[adm]['DateOfJoining'], substitute_teachers[adm]['Salary'], substitute_teachers[adm]['Age'], substitute_teachers[adm]['Qualifications'], substitute_teachers[adm]['Post'], substitute_teachers[adm]['Contact'], substitute_teachers[adm]['YearsOfContract']])
                                                                
                                                                print("Sorted list is produced in text file")
                                                                i=input("Want sorted list print? \nY/N:")
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
                                                                    if int(substitute_teachers[adm]["DateOfJoining"][0:4:1])<=year:
                                                                        te2.add_row([adm, substitute_teachers[adm]['name'], substitute_teachers[adm]['DateOfJoining'], substitute_teachers[adm]['Salary'], substitute_teachers[adm]['Age'], substitute_teachers[adm]['Qualifications'], substitute_teachers[adm]['Post'], substitute_teachers[adm]['Contact'], substitute_teachers[adm]['YearsOfContract']])
                                                                print("Sorted list is produced in text file")
                                                                i=input("Want sorted list print? \nY/N:")
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
                                                                    i=input("Want sorted list print? \nY/N:")
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
                                                                    i=input("Want sorted list print? \nY/N:")
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
                                                                    i=input("Want sorted list print? \nY/N:")
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
                                                                    i=input("Want sorted list print? \nY/N:")
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
                                                                        if substitute_teachers[adm]["Age"]==year:
                                                                            te2.add_row([adm, substitute_teachers[adm]['name'], substitute_teachers[adm]['DateOfJoining'], substitute_teachers[adm]['Salary'], substitute_teachers[adm]['Age'], substitute_teachers[adm]['Qualifications'], substitute_teachers[adm]['Post'], substitute_teachers[adm]['Contact'], substitute_teachers[adm]['YearsOfContract']])
                                                                    print("Sorted list is produced in text file")
                                                                    i=input("Want sorted list print? \nY/N:")
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
                                                                    
                                                                    for adm in substitute_teachers.keys():
                                                                        if substitute_teachers[adm]["Age"]<=year:
                                                                            te2.add_row([adm, substitute_teachers[adm]['name'], substitute_teachers[adm]['DateOfJoining'], substitute_teachers[adm]['Salary'], substitute_teachers[adm]['Age'], substitute_teachers[adm]['Qualifications'], substitute_teachers[adm]['Post'], substitute_teachers[adm]['Contact'], substitute_teachers[adm]['YearsOfContract']])
                                                                    print("Sorted list is produced in text file")
                                                                    i=input("Want sorted list print? \nY/N:")
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
                                                        te2 = PrettyTable()
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
                                                                            te2.add_row([adm, substitute_teachers[adm]['name'], substitute_teachers[adm]['DateOfJoining'], substitute_teachers[adm]['Salary'], substitute_teachers[adm]['Age'], substitute_teachers[adm]['Qualifications'], substitute_teachers[adm]['Post'], substitute_teachers[adm]['Contact'], substitute_teachers[adm]['YearsOfContract']])
                                                                    
                                                                    print("Sorted list is produced in text file")
                                                                    i=input("Want sorted list print? \nY/N:")
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
                                                                    i=input("Want sorted list print? \nY/N:")
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
                                                                    i=input("Want sorted list print? \nY/N:")
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
                        elif ch1==3:
                            while True:
                                line()
                                Students()
                                line()
                            
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
                                        else:
                                            print("Last attempt to enter valid admission no.")
                                            s_admno=input("Enter Admission no. of New Student:")
                                            if eh(s_admno)==False:
                                                print("You're exiting..")
                                                break
                                            else:
                                                s_admno=int(s_admno)
                                        s_name=input("Enter Name of New Student:")
                                        s_age=input("Enter Age:")
                                        if eh(s_age):
                                            s_age=int(s_age)
                                        else:
                                            print("Last attempt to enter valid student's age")
                                            s_age=input("Enter Age:")
                                            if eh(s_age)==False:
                                                print("You're exiting..")
                                                break
                                            else:
                                                s_age=int(s_age)

                                        s_class=input("Enter Class:")
                                        if eh(s_class):
                                            s_class=int(s_class)
                                        else:
                                            print("Last attempt to enter valid student's class")
                                            s_class=input("Enter Class:")
                                            if eh(s_class)==False:
                                                print("You're exiting..")
                                                break
                                            else:
                                                s_class=int(s_class)
                                
                                        gender()
                                
                                        s_gender=input("Enter gender:")
                                        s_gender=s_gender.title()
                                        s_dob=input("Enter DOB: DD/MM/YYYY")
                                        s_doa=input("Enter Date Of Admission:")
                                        s_contact="+91-"+input("Enter Contact No.")
                  
                                        #updated dictionary
                                        students[s_admno]={
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
                                
                                            while True:
                                                u_Students()
                                                ch5=input("Enter your choice:")
                                                if eh(ch5):
                                                    ch5=int(ch5)
                                    
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
                                        
                                                    print("Alphabetically sorted list is produced in text file.")
                                                    k1=input("If you want print here type Y else press enter: ")
                                                    if k1=="Y":
                                                        print(st2)
                                                    file.write("Alphabetically sorted list of students \n")
                                                    file.write(str(st2))
                                                    file.write("\n")

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
                                                            
                                                            print("Sorted list is produced in text file.")
                                                            k1=input("If you want print here type Y else press enter: ")
                                                            if k1=="Y":
                                                                print(st2)
                                                            
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
                                        
                                                            print("Sorted list is produced in text file.")
                                                            k1=input("If you want print here type Y else press enter: ")
                                                            if k1=="Y":
                                                                print(st2)
                                                                
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
                                                            print("Sorted list is produced in text file.")
                                                            k1=input("If you want print here type Y else press enter: ")
                                                            if k1=="Y":
                                                                print(st2)
                                                                
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
                                        
                                                        print("Sorted list is produced in text file.")
                                                        k1=input("If you want print here type Y else press enter: ")
                                                        if k1=="Y":
                                                            print(st2)
                                                                
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
                                                    
                                                    s_gender=input("Enter Choice: ")
                                                    if eh(s_gender):
                                                        s_gender=int(s_gender)
                                                        
                                                        if s_gender==1:
                                                            for adm in students.keys():
                                                                if students[adm]["gender"]=="Male":
                                                                    st2.add_row([adm, students[adm]['name'], students[adm]['age'], students[adm]['class'], students[adm]['gender'], students[adm]['DOB'], students[adm]['DateOfAdmission'], students[adm]['Contact']])

                                                            print("Sorted list is produced in text file.")
                                                            k1=input("If you want print here type Y else press enter: ")
                                                            if k1=="Y":
                                                                print(st2)
                                                                
                                                            file.write("Class-wise sorted list: \n")
                                                            file.write(str(st2))
                                                            file.write("\n")
                                                        
                                                        elif s_gender==2:
                                                            for adm in students.keys():
                                                                if students[adm]["gender"]=="Female":
                                                                    st2.add_row([adm, students[adm]['name'], students[adm]['age'], students[adm]['class'], students[adm]['gender'], students[adm]['DOB'], students[adm]['DateOfAdmission'], students[adm]['Contact']])

                                                            print("Sorted list is produced in text file.")
                                                            k1=input("If you want print here type Y else press enter: ")
                                                            if k1=="Y":
                                                                print(st2)
                                                                
                                                            file.write("Class-wise sorted list: \n")
                                                            file.write(str(st2))
                                                            file.write("\n")
                                                            
                                                        elif s_gender==3:
                                                            for adm in students.keys():
                                                                if students[adm]["gender"]=="Others":
                                                                    st2.add_row([adm, students[adm]['name'], students[adm]['age'], students[adm]['class'], students[adm]['gender'], students[adm]['DOB'], students[adm]['DateOfAdmission'], students[adm]['Contact']])

                                                            print("Sorted list is produced in text file.")
                                                            k1=input("If you want print here type Y else press enter: ")
                                                            if k1=="Y":
                                                                print(st2)
                                                                
                                                            file.write("Class-wise sorted list: \n")
                                                            file.write(str(st2))
                                                            file.write("\n")
                                                            
                                                        else:
                                                            print("Please enter an valid option")
                                                            print("You're exiting")
                                                            break
                                    
                                                file.close()

                                            #for sorting students year of admission
                                            elif ch7==5:
                                                with open("students_sorted.txt", "a") as file:
                                                    st2= PrettyTable()
                                                    st2.field_names = ["Admission No.", "Name of Student", "Age", "Class", "Gender", "DOB", "DateOfAdmission", "Contact"]
                                                    s_year=input("Enter Year of Admission:")
                                                    
                                                    for adm in students.keys():
                                                        if len(s_year)==4:
                                                            if students[adm]["DateOfAdmission"][6::1]==s_year:
                                                                st2.add_row([adm, students[adm]['name'], students[adm]['age'], students[adm]['class'], students[adm]['gender'], students[adm]['DOB'], students[adm]['DateOfAdmission'], students[adm]['Contact']])
                                                        
                                                        else:
                                                            print("Please enter an valid option")
                                                            print("You're exiting")
                                                            break
                                                    
                                                    print("Sorted list is produced in text file.")
                                                    k1=input("If you want print here type Y else press enter: ")
                                                    if k1=="Y":
                                                        print(st2)
                                                                
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
                                        print("You're logging out from Students Database")
                                        break
                 
            #wrong captcha
            elif captcha==False:
                print("Invalid Captcha")
                print(input("Press Enter To Exit \n"))
                print("Thanks For Using School Management System")

            #wrong id and password
            elif login[id_l]!=passw:
                print("Wrong id or password")
                print(input("Press Enter To Exit \n"))
                print("Thanks For Using School Management System")

            else:
                print("An error occured. \nPlease try again!")
                break

        #for updating password
        elif ch1==3:
            while True:
                id_u=input("Enter Your ID:")
                if id_u in login.keys():
                    pass_u1=input("Enter New Password: ")
                    p1(pass_u1)
                    pass_u2=input("Enter New Password Again: ")
                    if pass_u1==pass_u2 and verify():
                        login[id_u]=pass_u2
                        print("Password updated succesfully")
                        break
                    else:
                        continue
                else:
                    print("ID not found in database")
                    break

        #for deleting ID
        elif ch1==4:
            while True:
                id_d=input("Enter ID to be deleted:")
                pass_d=input("Enter ID's password")
                if id_d in login.keys():
                    if login[id_d]==pass_d and verify():
                        del login[id_d]
                        print("ID deleted successfully")
                        break
                    else:
                        print("Password or captcha is wrong! \nPlease Try Again")
                        continue
                else:
                    print("ID doesn't exists")

        #for report card
        elif ch1==5:
            info()
            while True:
                r_school=input("Enter school name: ")
                r_adm=input("Enter Student's Admission Number: ")
                if eh(r_adm)==False:
                    break
                else:
                    r_adm=int(r_adm)
                r_name = input("Enter student's name: ")
                r_class = input("Enter class: ")
                r_section = input("Enter section: ")
                r_mother_name = input("Enter mother's name: ")
                r_father_name = input("Enter father's name: ")
                r_contact= "+91-"+input("Enter contact number: ")
                r_gender = input("Enter gender: ")
                r_roll = input("Enter roll number: ")
                r_teacher=input("Enter class teacher's name: ")

                #table
                table = PrettyTable()

                table.field_names = ["Field", "Value"]
                table.add_row(["Admission Number", r_adm])
                table.add_row(["Name", r_name])
                table.add_row(["Class", r_class])
                table.add_row(["Section", r_section])
                table.add_row(["Mother's Name", r_mother_name])
                table.add_row(["Father's Name", r_father_name])
                table.add_row(["Contact Number", r_contact])
                table.add_row(["Gender", r_gender])
                table.add_row(["Roll Number", r_roll])
                table.add_row(["Class Teacher's Name", r_teacher])


                table.align = "l"

                marks={

                }
                
                n=input("Enter no. of subjects: ")
                if eh(n):
                    n=int(n)
                else:
                    break

                j=int(input("Enter maximum marks of all subjects together:"))

                
                while n>0:
                    r_sub=input("Enter subject: ")
                    r_sub_marks=int(input("Enter marks: "))
                    marks[r_sub]=r_sub_marks
                    n-=1

                report=PrettyTable()
                report.field_names = ["Subject", "Marks"]
                for subject, mark in marks.items():
                    report.add_row([subject, mark])

                l=sum(marks.values())
                
                if l>j:
                    print("Invalid input")
                    continue
                
                else:
                    per=(l/j)*100
                    if per>=90:
                        grade="A+"
                        remark="Great Going! Keep it up"
                        rep=f"{r_name} passed with {per}% in {r_class}."
                    elif per>=80:
                        grade="A"
                        remark="Great Going! "
                        rep=f"{r_name} passed with {per}% in {r_class}."
                    elif per >= 70:
                        grade = "B+"
                        remark = "Well done!"
                        rep = f"{r_name} passed with {per}% in {r_class}."
                    elif per >= 60:
                        grade = "B"
                        remark = "You can do better!"
                        rep = f"{r_name} passed with {per}% in {r_class}."
                    elif per >= 50:
                        grade = "C"
                        remark = "Focus on improving!"
                        rep = f"{r_name} passed with {per}% in {r_class}."
                    elif per >= 40:
                        grade = "D"
                        remark = "Work harder!"
                        rep = f"{r_name} passed with {per}% in {r_class}."
                    else:
                        grade = "F"
                        remark = "Failed!"
                        rep = f"{r_name} failed with {per}% in {r_class}."


                with open(f"{r_name}_report.txt", 'w') as file:
                    file.write(f"{r_school} \n")
                    file.write("Student's Details:")
                    file.write("\n")
                    file.write(str(table))
                    file.write("\n")
                    file.write(str(report))
                    file.write("\n")
                    file.write(f"Grade: {grade} \n")
                    file.write(f"Remarks: {remark} \n")
                    file.write(f"Conclusion: {rep} \n")
                    file.write("Thank You!")
                file.close

                print("Want to make another report card or exit?")
                print("If exit press enter else write Y.")
                h=input("Enter you choice: ")
                if h=="Y":
                    continue
                else:
                    break

        #for salary-slip making
        elif ch1==6:
            while True:
                teacher_name=input("Enter Teacher's Name: ")
                teacher_id=input("Enter Teacher's ID: ")
                basic_salary=int(input("Enter Basic Salary: "))
                allowance=int(input("Enter Allowance:"))
                teacher_post=input("Enter Post of Teacher:")
                teacher_doj=input("Enter DOJ: ")
                file_name=f"{teacher_name}_salaryslip.txt"
                generate_salary_slip(teacher_name, teacher_id, basic_salary, allowance, file_name, teacher_post, teacher_doj)

                print("Want to make another salary slip or exit?")
                print("If exit press enter else write Y.")
                h=input("Enter you choice: ")
                if h=="Y":
                    continue
                else:
                    break

        elif ch1==7:
            while True:
                print("UID of student is admission number.")
                print("Password is first 2 letters of name and year of birth.")
                print("For Example: If name is Gracy and year of birth is 2010. \nThen the password will be Gr2010.")
                login_enter=input("Enter UID of Student")
                if eh(login_enter):
                    login_enter=int(login_enter)
                    if login_enter in students.keys():
                        password=students[login_enter]["name"][0:2] + students[login_enter]["DOB"][-4:]
                        password_enter= input("Enter password: ")
                        if password==password_enter:
                            if verify():
                                print("Login Successful")

                                fees()

                                ch=input("Enter Your Choice")
                                if eh(ch):
                                    ch=int(ch)
                                    fees_paid=False
                                    if ch==1:
                                        if students[login_enter]["class"]<=2:
                                            p=3000
                                            print("Amount Due: ", p)
                                            fees_paid=pay_amount(p)
                                            break
                                        if students[login_enter]["class"]<=5 and students[login_enter]["class"]>=3:
                                            p=6000
                                            print("Amount Due: ", p)
                                            fees_paid=pay_amount(p)
                                            break
                                        if students[login_enter]["class"]<=8 and students[login_enter]["class"]>=6:
                                            p=9000
                                            print("Amount Due: ", p)
                                            fees_paid=pay_amount(p)
                                            break
                                        if students[login_enter]["class"]<=10 and students[login_enter]["class"]>=9:
                                            p=12000
                                            print("Amount Due: ", p)
                                            fees_paid=pay_amount(p)
                                            break
                                        if students[login_enter]["class"]<=12 and students[login_enter]["class"]>=11:
                                            p=15000
                                            print("Amount Due: ", p)
                                            fees_paid=pay_amount(p)
                                            break
                                    
                                    elif ch==2:
                                        
                                        if students[login_enter]["class"]<=2 and students[login_enter]["class"]>=1:
                                            p=3000
                                        if students[login_enter]["class"]<=5 and students[login_enter]["class"]>=3:
                                            p=6000
                                        if students[login_enter]["class"]<=8 and students[login_enter]["class"]>=6:
                                            p=9000
                                        if students[login_enter]["class"]<=10 and students[login_enter]["class"]>=9:
                                            p=12000
                                        if students[login_enter]["class"]<=12 and students[login_enter]["class"]>=11:
                                            p=15000
                                        
                                        student_id = login_enter
                                        
                                        if fees_paid==True:
                                            generate_fee_receipt(student_id, p)
                                            print("Fee Receipt is Generated.")
                                            break
                                        else:
                                            print("Fee Receipt is not Generated.")
                                            print("Pay fees first")
                                            continue

                                    else:
                                        print("Logging Out...")
                                        break
                                            

                            else:
                                print("Wrong Captcha!")
                                print("Exiting...")
                                break
                        else:
                            print("Wrong Password!")
                            break
                    else:
                        print("Login ID doesn't exists.")
                        print("Please try again!")
                        break

        #for exiting
        else:
            print("Logging Out...")
            break
