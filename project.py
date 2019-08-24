# Give the user the following options.
# Once the option that is selected is completed keep asking them until
# they hit 4 to quit:

# Hello, please choose one of following options:
# 1) Check balance
# 2) Add money to account
# 3) Withdraw money from account
# 4) Quit
# What will you like to do?
pinnumber = 5555 # !! : this should not be hardcoded 
username = "flashfan" # !! : this should not be hard coded

# Username prompt goes here
userInput1 = input("Please enter your username")
while userInput1 != username:
    if userInput1 != username: # !! : this is redundant 
        print("Incorrect username")
    # !! : update the conditional value in a while loop (this is an infinte loop)

# Pin number prompt goes here
userInput2 = int(input("Enter your Pin Number"))
while userInput2 != pinnumber:
    print("Incorrect Pin")
    # !! : update the conditional value in a while loop (this is an infinte loop)

# User Options goes here
userInput = int(input('Hello, please choose one of the following options:'
                      '\n1) Check balance'
                      '\n2) Add money to account'
                      '\n3) Withdraw money from account'
                      '\n4) Quit'))
balance = 0 # !! : balnce should be updated INSIDE the loop
while userInput != 4:
    userInput = int(input('Hello, please choose one of the following options:'
                          '\n1) Check balance'
                          '\n2) Add money to account'
                          '\n3) Withdraw money from account'
                          '\n4) Quit'))
    if userInput == 1:
        print(f"Your current balance is {balance}")
    elif userInput == 2:
        userInput = int(input('How much money would you like to deposit?'))
        print(f'Your new balance is {balance + userInput}')
        # !! : update the value of balance
    if userInput == 3:
        userInput = int(input('How much money would you like to withdraw?'))
        print(f'You now have {balance - userInput}')
        # !! : updat the value of balance AND check that the user has sufficent funds






