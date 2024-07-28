while True:
    # Get card type from user
    Card_Type = input("Enter your ATM Card Type (Visa, Mastercard, Rupay, Maestro) or 'exit' to quit: ")

    if Card_Type == "exit":
        print("Exiting the ATM system.")
        break

    # Get transaction type from user
    Transaction_Type = input("Enter Your Transaction Type (Withdrawal, Deposit, Balance Inquiry, Mini Statement): ")

    Amount = ""
    Output = ""

    if Card_Type == "Visa":
        if Transaction_Type == "Withdrawal":
            Amount = input("Enter the Amount: ")
            Output = "Transaction Successful"
        elif Transaction_Type == "Deposit":
            Amount = input("Enter the Amount: ")
            Output = "Transaction Successful"
        elif Transaction_Type == "Mini statement":
            Output = "Print Balance Amount as Receipt"
            Amount = 0
        elif Transaction_Type == "Balance Inquiry":
            Output = "Show User's Balance in Display"
            Amount = 0
        else:
            Output = "Transaction Cancelled"

    elif Card_Type == "Rupay":
        if Transaction_Type == "Withdrawal":
            Amount = input("Enter the Amount: ")
            Output = "Transaction Successful"
        elif Transaction_Type == "Deposit":
            Amount = input("Enter the Amount: ")
            Output = "Transaction Successful"
        elif Transaction_Type == "Mini statement":
            Output = "Print Balance Amount as Receipt"
            Amount = 0
        elif Transaction_Type == "Balance Inquiry":
            Output = "Show User's Balance in Display"
            Amount = 0
        else:
            Output = "Transaction Cancelled"

    elif Card_Type == "Mastercard":
        if Transaction_Type == "Withdrawal":
            Amount = input("Enter the Amount: ")
            Output = "Transaction Successful"
        elif Transaction_Type == "Deposit":
            Amount = input("Enter the Amount: ")
            Output = "Transaction Successful"
        elif Transaction_Type == "Mini statement":
            Output = "Print Balance Amount as Receipt"
            Amount = 0
        elif Transaction_Type == "Balance Inquiry":
            Output = "Show User's Balance in Display"
            Amount = 0
        else:
            Output = "Transaction Cancelled"

    elif Card_Type == "Maestro":
        if Transaction_Type == "Withdrawal":
            Amount = input("Enter the Amount: ")
            Output = "Transaction Successful"
        elif Transaction_Type == "Deposit":
            Amount = input("Enter the Amount: ")
            Output = "Transaction Successful"
        elif Transaction_Type == "Mini statement":
            Output = "Print Balance Amount as Receipt"
            Amount = 0
        elif Transaction_Type == "Balance Inquiry":
            Output = "Show User's Balance in Display"
            Amount = 0
        else:
            Output = "Transaction Cancelled"

    else:
        Output = "Invalid Card Type"

    # Print results
    print(f"Your card type is: {Card_Type}")
    print(f"Your Withdrawal or Deposited Amount: {Amount}")
    print(f"Your Final Output is: {Output}")