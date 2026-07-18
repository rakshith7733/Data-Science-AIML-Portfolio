#Creating a empty dictionary to store student data.
student = {}

#Creating a function for adding student information.
def add_student():
    "Adding Student Information into Records."

    #Taking roll number input
    roll = int(input("Enter the Roll Number: "))

    #Roll number is unique so checking if roll number already exists in the record.
    if roll in student:
        print("Roll Number is already Exists. Validate you roll number<?>")
        return

    #Taking the student name as input
    name = input("Enter the student name: ")

    #Creating marks list.
    marks = []

    print("Enter 5 Subject Marks.")
    for i in range(1,6):
        #We are taking inputs of the subject marks.
        m = int(input(f" Subject {i}: "))

        # If same marks comes it will just add to marks rather than overwriting the existing one.
        marks.append(m)

        #We are assigning the name & marks to roll number
        student[roll] = {
            'name': name,
            'marks': marks
        }
    #Confirmation message.
    print("Your Data is Saved Successfully.......")

#Creating a function to display the recorded information.
def display():
    "//Display Student Information//"

    #Checking if there is information already available in the records to fetch.
    if len(student) == 0:
        print("No Student Information Found!!")
        return

    #Creating a loop on dictionary to fetch the roll associated information.
    #Items pull the information in key and value format.
    for stud_id, stud_data in student.items():

        #We are calculating the Total marks and the percent direct in the display section.
        total = sum(stud_data['marks'])
        percent = total / len(stud_data['marks'])

        print("===========================================Student~List================================================")

        #Display format of student information.
        print(f"Student Id: {stud_id}")
        print(f"Student Name: {stud_data['name']}")
        print(f"Student Marks: {stud_data['marks']}")
        print(f"Student Total Marks: {total}")
        print(f"Overall Percentage: {percent}%")


#Creating a function for the deleting information.
def del_student():

    #We will take the student information to be deleted. So we will go with ID which is unique.
    roll = int(input("Enter the Roll Number: "))

    #Checking if the student data is already present in the records.
    if roll not in student:
        print("Student Not Found")
        return

    print("\n====================Student Information===============================\n")
    print("Student Information: ", student[roll]['name'])

    #To take confirmation from user are they agree to proceed further action.
    confirm = input("Are you sure you want to delete the student information: (Y/N)").lower()

    if confirm == 'y':
        print(f"Student {student[roll]['name']} is successfully deleted")
        del student[roll]
    else:
        print("Deletion action cancelled.")
        return

#Default function to show the Menu details until user is tired.
def main():
    
    #Until user input exit the loop will run infinity times.
    while True:
        print("======================================================================================================================")
        print("=================================== Welcome to Student Information System! ===========================================")
        print("======================================================================================================================")

        print("====MENU====")
        print("1. Add Student\n2. Display Student\n3. Delete Student\n4. Exit ")

        choice = int(input("Enter the choice: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            display()
        elif choice == 3:
            del_student()
        elif choice == 4:
            print("Thanks for your response. Exiting")
            break
        else:
            print("Invalid response...")

#Calling the main function
main()
