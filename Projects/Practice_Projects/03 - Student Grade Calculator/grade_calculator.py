#Student database
student_data = {}

#Function for percentage wise grade
def percentage_grade(percentage):
    "This will evaluate percentage with respective grade."

    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    elif percentage >= 50:
        return 'E'
    else:
        return 'F'


#def grade mapping according to gpa
def grade_mapping(grade):
    grade_map = {"A":5.0,'B':4.0,'C':3.0,'D':2.0,'E':1.0,'F':0.0}
    return grade_map.get(grade,0.0)      #get() method it lookup for key and if the key have value it print or else default will be assigned.


#Adding student data
def add_student():

    #we will take UID of the student for further lookups
    try:
        uid = input("Enter your user ID: ")
    except ValueError:
        print("UID must be numeric 3 digit value.")
        return

    #checking User ID if already exists in the records
    if uid in student_data:
        print("UID is already exists.")
        return

    #Taking name input
    name = input("Enter Student Name: ").strip()


    #marks list for storing marks records.
    marks = []

    print("Enter 5 subjects marks: ")
    for mark in range(1,6):
        try:
            #Taking 5 subject marks within loop
            m = int(input(f"Enter Subject {mark} marks: "))

        except ValueError:
            print("Marks must be numeric.")
            return

        #Marks can't be negative or more than 100 as our threshold is 100.
        if m < 0 or m > 100:
            print("Invalid mark details.")
            return

        #we will take the marks that user give and assign to our marks list.
        marks.append(m)



    #Calculations
    total_marks = sum(marks)    #we are taking marks directly as it is local varaiable and we have not yet assigned to dictionary.
    percentage = total_marks / len(marks)
    grade = percentage_grade(percentage)
    gpa = grade_mapping(grade)


    #We will add the data to our student dictionary database with UID as Unique ID to lookup.
    student_data[uid] = {
        'name':name,
        'marks':marks,
        'percentage':percentage,
        'grade':grade,
        'gpa':gpa
    }


    #Confirmation message for data saved.
    print("Data Succussfully Saved......")



def display():
    "Display student Information"

    try:
        uid = input("Enter your user ID: ")
    except ValueError:
        print("UID must be numeric 3 digit value.")
        return

    #Checking if uid is present in records.
    if uid not in student_data:
        print("No Information found.")
        return

    #we assign to student variable for unique ID for our fetch rather than from database.
    student = student_data[uid]

    print("\n"+"="*50)
    print(("  STUDENT REPORT CARD  "))
    print("="*50)
    print(f"UID  :  {uid}")
    print(f"Name  :  {student['name']}")
    print(f"Marks  :  {student['marks']}")
    print(f"Percentage  :  {student['percentage']:.2f}%")
    print(f"Grade  :  {student['grade']}")
    print(f"GPA  :  {student['gpa']}")
    print("="*50)


#leaderboard
def leaderborad():

    topper_list = sorted(student_data.items(), key=lambda item: item[1]['percentage'],reverse=True)

    print("Topper List")
    for rank, (uid,student) in enumerate(topper_list, start=1):
        print(f"Rank {rank}: {student['name']} - {student['percentage']}% - {student['gpa']}")


def main():
    "Main function where user menu and all function interlink."

    while True:
        print("="*50)
        print(" .WELCOME TO STUDENT GRADE CALCULATOR.")
        print("="*50)

        print("Menu:\n1.Add student \n2.Display \n3.Leaderboard \n4.Exit \n")

        try:
            #Taking user input to what operation he want to do
            user_choice = int(input("Enter your choice: "))

            if user_choice == 1:
                add_student()
            elif user_choice == 2:
                display()
            elif user_choice == 3:
                leaderborad()
            elif user_choice == 4:
                print("Thank you..")
                break
            
        except ValueError:
            print("Please enter a valid number between 1 to 4.")
            continue


#Calling the function
main()




