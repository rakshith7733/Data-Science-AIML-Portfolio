
# # 1. Initialize once (empty)
# records = defaultdict(list)

# # 2. Directly append new categories without defining them first
# records["Food"].append({"amount": 500, "date": "2026-07-18"}) 
# # "Food" key is created automatically here

# records["Travel"].append({"amount": 200, "date": "2026-07-19"}) 
# # "Travel" key is created automatically here

# # 3. Append to existing categories
# records["Food"].append({"amount": 50, "date": "2026-07-20"})

# print(dict(records))
# # Output: {'Food': [{...}, {...}], 'Travel': [{...}]}
#------------------------------------------------------------------------------------------------

from collections import defaultdict

#Database
# Initialize the main database once (outside the function ideally, but here for context)
# This dictionary will hold lists of records for each category
expenses = defaultdict(list)


# Add Expenses
def add_expense():
    "This Function is to add expense based on category with amount and date."

    #Taking first option as category so based on the category we add amount and date.
    category = input("Enter the category: ").strip()

    if not category:
        print("Please enter a valid category")
        return

    print(f"Please enter category '{category}' expense. Type 'done' once items added.\n")

    while True:

        #Taking amount and date
        amount_input = input("Enter the amount: ")

        if amount_input.lower() == 'done':
            break

        try:
            amount = int(amount_input)
            if amount < 0:
                print("Amount can't be negative.")
                continue

        except ValueError:
            print("Invalid Response.")
            continue

        #Taking date in DD/MM/YYYY
        dd = input("Enter Date in DD-MM-YYYY: ")  #15-08-2026


        #Taking local variable to store data and upload to main database later fetching
        record = {
            'amount':amount,
            'date':dd
            }

        expenses[category].append(record)

        print("Expense Saved Successfully..")


    print("Summary:\n")
    for item in expenses[category]:
        print(f"{item['amount']},{item['date']}")
        



# View Expenses
def view_expense():
    pass

# Delete Expense
def delete_expense():
    pass

# Overall Category Summary
def category_summary():
    pass

# Monthly Expense Total
def monthly_total():
    pass






def main():
    "Main function to call respective function module."

    while True:
        print("="*50)
        print("Welcome to Expense Tracker!")
        print("="*50)

        print("Menu:\n1. Add Expense \n2. View Expense \n3. Delete Expenses \n4. Category Summary \n5. Save to File \n6. Exit")

        try:
            user_choice = int(input("Enter your choice: "))

            if user_choice == 1:
                add_expense()
            elif user_choice == 2:
                view_expense()
            elif user_choice == 3:
                delete_expense()
            elif user_choice == 4:
                category_summary()
            elif user_choice == 5:
                monthly_total()
            elif user_choice == 6:
                print("Thank you.")
                break

        except ValueError:
            print("Please Enter Valid response.")
            continue


#Calling the main function
main()