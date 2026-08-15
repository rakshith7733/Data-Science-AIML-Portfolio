import json
from collections import defaultdict

#Database
# Initialize the main database once (outside the function ideally, but here for context)
# This dictionary will hold lists of records for each category.

try:
    with open('data.json','r') as f:
        data = json.load(f)
        expenses = defaultdict(list, {k: list(v) for k, v in data.items()})

except FileNotFoundError:
    expenses = defaultdict(list)


#Save data into json file.
def save_data():
    "This function saves the data added in expense to json file."

    with open("data.json",'w') as f:
        json.dump(dict(expenses),f)


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

    #Saving the data to json file for further retreival.
    save_data()

    print("Expense Saved Successfully....")


# View Expenses
def view_expense():
    "This function will result the display of the expenses stored."

    exp_check = input("Enter the Category Expenses you need to display: ").strip()

    if not exp_check:
        print("Enter correct category")
        return
    
    if exp_check in expenses:
        print("="*50)
        print(f"Expense Dashboard for {exp_check}")
        print("="*50)

        # check step by step for the category and pull respective category items and prints.
        for item in expenses[exp_check]:
            print(f"Category: ",item)
            print(f"Amount: {item['amount']}")
            print(f"Date: {item['date']}")
            print("~"*30)
    else:
        print(f"Category {exp_check} doesn't exist in record. Please choose the available Expenses {list(expenses.keys())}")
    
      

# Delete Expense
def delete_expense():
    "This function will delete the record of respective category bill/amount."

    #we will take the category item amount to be deleted.
    category = input("Enter the category: ").strip()


    #handle any case senstitivity values.
    found_key = next((k for k in expenses if k.lower() == category.lower()), None)
    
    if not category:
        print("Please enter a valid category")
        return

    print("Available Category's:\n")
    for i,record in enumerate(expenses[found_key]):
        print(f"{i} Amount: {record['amount']},Date: {record['date']}")


    try:
        target_amount = int(input("Enter the amount: "))
        target_date = input("Enter the respective amount date: ")

        for i, record in enumerate(expenses[found_key]):
            if record['amount'] == target_amount and record['date'] == target_date:
                del expenses[found_key][i] #deleting the record by index of amount and date combination.
                print("Data deleted Successfully..")

                #Save to the file
                save_data()
                return

        print("No matching record found with matching record of amount and date.")

    except ValueError:
        print("Enter valid amount.")
        return

# Overall Category Summary
def category_summary():
    "This function will calculate of category wise count, total amount spent" #food 1200 count:4, Grocery 1000 count 3

    #we will take the category item amount listed.
    category = input("Enter the category: ").strip()
    
    #handle any case senstitivity values.
    found_key = next((k for k in expenses if k.lower() == category.lower()), None)

    if not found_key:
        print(f"Expense record not found for {found_key}.")
        print(f"Expense record for {list(expenses.keys())}")
        return
    
    else:
        #We are taking this variable if the category is found the database, so based on the data we will do rest of the calculations.
        records = expenses[found_key]

        if not records:
            print(f"Expenses record for {found_key}present but no data available")
        else:
            total_amount = sum(record['amount'] for record in records)     #Total sum of the records for category.
            total_count = len(records)                                     #Total count of the records
            dates = [record['date'] for record in records]                 #Taking the date of the category later we will fetch start and end dates.


            print(f"=========Category Summary: {found_key}============")
            print(f"Total Amount: ${total_amount}")
            print(f"Total Number of Transactions: {total_count}")
            print(f"Average Transactions: ${total_amount/total_count:.2f}")

            if dates:
                print(f"Date Range: {min(dates)} to {max(dates)}")
            else:
                print("Date Range: N/A") 
    input("\nPress Enter to return to menu...")   

# Monthly Expense Total
def monthly_total():
    target_month = input("Enter the Month: ") #08
    target_year = input("Enter the Year: ")   #2026

    total_spend = 0
    count = 0

    for category, records in expenses.items():
        for record in records:

            parts = record['date'].split('-')
            if len(parts) == 3:
                day, month, year = parts

                if month == target_month and year == target_year:
                    total_spend += record['amount']
                    count += 1
    if count == 0:
        print(f"No Expenses found for {target_month}-{target_year}.")
    else:
        print("~"*50)
        print(f"Monthly Expense for {target_month}-{target_year}")
        print(f"Total Amount Spend: ${total_spend}")
        print((f"Total Transactions: {count}."))
        print("~"*50)

    input("\nPress Enter to return to menu...")


def main():
    "Main function to call respective function module."

    while True:
        print("="*50)
        print("Welcome to Expense Tracker!")
        print("="*50)

        print("Menu:\n1. Add Expense \n2. View Expense \n3. Delete Expenses \n4. Category Summary \n5. Monthly Total \n6. Exit\n")

        try:
            user_choice = int(input("Enter your choice: "))

            if user_choice == 1:
                add_expense() #done
            elif user_choice == 2:
                view_expense() #done
            elif user_choice == 3:
                delete_expense() #done
            elif user_choice == 4:
                category_summary() #done
            elif user_choice == 5:
                monthly_total() #done
            elif user_choice == 6:
                print("Thank you.") #done
                break

        except ValueError:
            print("Please Enter Valid response.")
            continue


#Calling the main function
main()