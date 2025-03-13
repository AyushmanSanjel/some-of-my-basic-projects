class Account:
    
    def __init__(self, bal, accno):
        self.balance= bal
        self.account=accno
   
    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"has been debited")
        print("TOTAL BALANCE :",self.get_balance())
   
    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"has been credited")
        print("TOTAL BALANCE :",self.get_balance())
    
    def get_balance(self): 
        return self.balance
acc1 = Account(10000, 234)

acc2= Account(100000, 345)

acc3= Account(100000000, 980)

acc4= Account(10000000000, 3126)

pass 
accounts_no=(int(input("PLEASE TELL YOUR ACCOUNT NUMBER = ")))
if accounts_no == 234:
     selected_account = acc1
elif accounts_no == 345:
    selected_account = acc2
elif accounts_no == 980:
    selected_account= acc3
elif accounts_no == 3126:
    selected_account=acc4
else:
    print("Invalid account number!")

service = input('please enter the service you want ')


if service == 'balance enquiry':
    if accounts_no == 234:
        print("Your current balance is: Rs.", selected_account.get_balance())
    elif accounts_no == 345:
        print("Your current balance is: Rs.", selected_account.get_balance())
    elif accounts_no == 980:
        print("Your current balance is: Rs.", selected_account.get_balance())
    elif accounts_no == 3126:
        print("Your current balance is: Rs.", selected_account.get_balance())   
    else:
        print("PLEASE ENTER A VALID ACCOUNT NUMBER")

elif service == "debit or credit":
    
    operation=input("Enter the choice 'DEBIT'or'CREDIT'")

    if (operation == "debit"):
        selected_account.debit(int(input("enter the amount")))
    elif(operation == "credit"):
        selected_account.credit(int(input("enter the amount")))
    else:
        print("SORRY WE DON'T HAVE THE AUTHORITY")

    print("THANK YOU FOR VISITING US !!!!!!!!")
else:
    print("SORRY WE DON'T HAVE THIS SERVICE AVAILABLE IN OUR SYSTEM ")