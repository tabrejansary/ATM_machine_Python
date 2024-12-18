def check_balance():
    print(f"Your current balance is ${balance:.2f}")
def withdraw():
    amount=float(input("Enter the amount to be Withdrawn"))
    if amount>balance:
        print("Insufficient Funds ")
        return 0
    elif amount<0:
        print("THe AMount must be greater than 0")
        return 0
    else:
        return amount
def enter_pin():
    entered_pin=input("Enter your ATM PIN")
    if entered_pin==atm_pin:
        print("Now you can access the following Services")
        return True
    else:
        print("Incorrect PIN.Access Denied")
     
def change_pin():
    global atm_pin
    current_pin=input("Enter your current PIN")  
    if current_pin==atm_pin:
        new_pin=input("Enter your new pin")
        confirm_pin=input("Enter your new PIN again for confirm")
        if new_pin==confirm_pin:
            atm_pin=new_pin
            print("ATM PIN Changed")   
        else:
            print("New PIN DOesn't match with the confiemation PIN")
    else:
        print("Wrong PIN") 

def deposit():
    amount=float(input("Enter the amount you want to deposit:"))
    if amount<0:
        print("Thats not the Valid amount")
        return 0
    elif amount>400000:
        print("Thats very high amount ,Sorry you can't deposit via ATM")
        return 0
    else:
        return amount
atm_pin='1234'
balance=0
is_running=True
while is_running:
    print("\ATM Machine")
    if enter_pin():
        print("ATM Machine")
        print("1.Check Balance")
        print("2.WIthdraw")
        print("3.Depost Money")
        print("4.Change PIN")
        print("5.Exit")

        choice=input("Enter your Choice (1-4)")

        if choice=='1':
            check_balance()
        elif choice=='2':
            balance-=withdraw()
        elif choice=='3':
            balance+=deposit()
        elif choice=='4':
            change_pin()
        elif choice=='5':
            is_running=False 
        else:  
            print("This is invalid Choice")

    print("Thank you.Have a nice day")
        
