from atm import accounts
from atm import transaction
class menu:
    accid = ""
    def start(self):

        a = accounts.accounts()
        b = transaction.transaction()
        while True:
            print("Welcome to bank of nova scotia ATM")
            try:
                id=input("Enter your account id: ")
                name=a.accountverify(id)
                print("Welcome ",name)
                menu.accid=id
                pin=input("Enter your pin number: ")
                if a.pinverify(pin):
                    self.atmservice()
            except Exception as e:
                print("Error: ",e)
            del a
            del b

    def atmservice(self):
        a = accounts.accounts()
        b = transaction.transaction()
        while True:
            print("ATM service...")
            print("1.Deposit money")
            print("2.Withdraw money")
            print("3.Transaction list")
            print("0.End transaction")
            opt=int(input("Enter your option: "))

            if opt==1:
                amount=int(input("Enter the amount to be deposited: "))
                b.deposit(menu.accid,amount)
            elif opt==2:
                amount = int(input("Enter the amount to be withdrawn: "))
                b.withdraw(menu.accid, amount)
            elif opt==3:
                b.listtransaction(menu.accid)
            elif opt==0:
                break
            else:
                print("Invalid option Try again...")