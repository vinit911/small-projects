'''
Royal Kids Bank 
Vinit's COde
All copyright reserve 
Design a Banking App in Python that has the following functionalities:-
User can:-
◆OPEN ACCOUNT by username and password of his choice. On Opening account, his initial balance will be ₹ 25,000/-. Once he opens account, he can login by re-entering the same username & password.
◆LOGIN is compulsory to perform any task such as withdrawal, deposit or balance check. If the user name or password do not match, he can not Login. Once he is logged in, he can do as many transactions as he wants. He needs to Logout after he finishes all the transactions
◆DEPOSIT will enable user to deposit amount of money of his choice. His balance should be updated after the task completes.
◆WITHDRAW will enable user to withdraw amount of money of his choice. The only condition is that his balance at any point can not go less than ₹10,000/-. If this can happen after his withdrawal, your program must not allow that transaction. His balance should be updated after the task completes.
◆
From Namra Shah to Everyone:  06:18 PM
◆CHECK BALANCE will show the latest updated balance to user.
◆LOGOUT will exit the user from the program
You should use these functions in your program: login(), deposit(), withdraw(), checkBalance()
'''


def login():
    a = 0
    name = input("Please enter your name :- ")
    password = input("Please enter your password :- ")
    verifyName = input("verify your name :- ")
    verifyPassword = input("verify your password :- ")
    if(verifyName == name and verifyPassword == password and verifyName != '\0' and verifyPassword != '\0' and name != '\0' and password != '\0'):
            print("Success fully loged in ")  
            print("-----------------------------------------------------------------------")
            a = 1
            return a
            

    else:
        print("Enter the correct pass")
        for x in range(0,3):
            verifyName = input("verify your name :- ")
            verifyPassword = input("verify your password :- ")
        
            if(verifyName == name and verifyPassword == password):
                print("Success fully loged in ")
                print("-----------------------------------------------------------------------")
                a = 1
                return a
                
            else:
                print(f"You got {x-3} chance left")
                print("You lost your 3 chance")

    
    

def deposit(initialbalance):
    print(f"Your intial balance is {initialbalance} Rs")
    amount_deposit = int(input("Enter the amount you want to deposit :- "))
    initialbalance = initialbalance + amount_deposit
    print("Your new balance is ",initialbalance)
    return initialbalance

def withdraw(initialbalance):
    print(f"Your intial balance is {initialbalance} Rs")
    amount_withdraw = int(input("Enter the amount you want to withdraw :- "))
    initialbalance = initialbalance - amount_withdraw
    if(initialbalance >= 10000):
        print("Your new balance is = ",initialbalance)
    else:
        newcurrentbalance = initialbalance - amount_withdraw
        print(f"If you withdraw this amount your would be {newcurrentbalance} and according to banks policy minimum balance must be greater or equal to 10000 ")
        
    return initialbalance
    
def checkBalance():
    print("Your current balance is ",initialbalance)

   

a = login()

if (a == 1):


    initialbalance = int(input("Enter your first deposit "))

    for x in range(0,10):

        print("1.....Deposit\n2.....Withdraw\n3.....Checkbalance\n4....log Out")
        option = int(input("Choice our service :- "))
        if(option == 1):
            newdeposit = deposit(initialbalance)
            print("Thanks for using our service")
            initialbalance = newdeposit
            print(initialbalance)
        
            

        elif(option == 2):
            newwithdraw = withdraw(initialbalance)
            print("Thanks for using our service")
            
            initialbalance = newwithdraw
            


        elif(option == 3):
            checkBalance()
            print("Thanks for using our service")
            

        elif(option == 4):
            exit()
