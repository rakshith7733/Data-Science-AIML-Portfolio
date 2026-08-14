#ATM Management System                              |
#Features: Deposit,Withdraw, check balance, Exit.   |
#===================================================|

#Creating empty dictionary to store account details
account = {}

def add_money(balance):
    "We deposit money if account number is given/exists."

    #We take account number to store the deposit information.
    acc_num = input("Enter you Account Number: ")

    if len(acc_num) != 9:
        print("Please Enter a valid Account Number. Account number consists of 9 digits.")
        return

    #We will ask user how much money he wants to deposit.
    amount = float(input("Enter the Deposit number: "))

    print(f"You have Entered the Amount: ${amount}")

    # we are adding the money to account number
    balance += amount
    print(f"Your Account Balance: {balance}\n")

    #Giving confirmation that money is added to the account
    print("Your money is Successfully Deposited<!>")

    account[acc_num] = {
        'account number': acc_num,
        'deposit': balance
    }
    return balance

#-----------------------------------------------------------------------------------------------------------------------
def display(balance):
    "Check Balance"
    acc_num = input("Enter you Account Number: ")
    if acc_num not in account:
        print("Account Number Doesn't Exists.")
        return

    print(f"|===========Account Balance===========|")
    print(f"|  Account Number    ||   {acc_num}   |")
    print(f"|  Available Balance ||  ${balance}   |")
    print(f"|====================||===============|\n")

#-----------------------------------------------------------------------------------------------------------------------
def withdraw(balance):
    "Withdrawal Balance"
    #choose account number
    #based on that how he want to withdraw
    #if amount exits in account deduct for withdrawal
    #if amount doesn't exist show 'No Fund available' return

    acc_num = input("Enter you Account Number: ")

    #Checking for Account confirmation
    if acc_num not in account:
        print("Account Number Doesn't Exists.")
        return

    #Checking for balance availability
    if balance == 0:
        print(f"Don't have enough Fund in Account:{acc_num}")
        return balance

    wid_amount = float(input("Enter the Withdrawal Amount: "))
    #Checking if withdraw amount is exceeding the availability amount in account.
    if wid_amount > balance:
        print(f"Insufficient Balance amount.\n Current Balance: {balance}")
        return balance
    else:
        balance -= wid_amount
        print("Withdrawal Successfully.")
        print("Available Balance: $",balance)
        return balance

#-----------------------------------------------------------------------------------------------------------------------
#Creating a main function to initial process. main heart
def main():

    # Creating a money variable to hold money deposited by customer.
    balance = 0

    while True:
        print("=============================================================================")
        print("===========================ATM Management System=============================")
        print("=============================================================================")

        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Cancel Transaction")
        options = int(input("Please choose you option:"))

        if options == 1:
            balance = add_money(balance)
        elif options == 2:
            balance = withdraw(balance)
        elif options == 3:
            display(balance)
        elif options == 4:
            print("Thanks for using DIF ATM. Please Visit..")
            break
        else:
            print("Invalid Respose.......")
            return

#calling our main function
main()