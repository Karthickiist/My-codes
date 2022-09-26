from datetime import datetime
filename="./data/transaction.txt"
class transaction:
    def deposit(self,id,amount):
        time=datetime.now().strftime("%d/%m/%y  %X")
        with open(filename,"a") as f:
            f.write("{},{},deposit,{} ".format(id,time,amount))
            f.write("\n")

    def withdraw(self,id,amount):
        time = datetime.now().strftime("%d/%m/%y  %X")
        with open(filename, "a") as f:
            if self.balance(id)>0:
                f.write("{},{},withdraw,{} ".format(id, time, amount))
                f.write("\n")
            else:
                print("Insufficient fund...")
                print("Thank you")

    def listtransaction(self,id):
        with open(filename,"r") as f:
            line=f.readlines()
            print("Trarnsaction list...")
            print("--------------------------------")
            for i in line:
                if i.strip()!="":
                    temp=i.split(",")
                    if temp[0]==id:
                        if temp[2]=="withdraw":
                            temp[3]="-"+temp[3]
                        print("{}     {}".format(temp[1], temp[3]))
        print("------------------------------------")
        print("Available balance: ",self.balance(id))

    def balance(self,id):
        balance=0
        with open(filename, "r") as f:
            line=f.readlines()
            for i in line:
                if i.strip()!="":
                    temp=i.split(",")
                    if temp[0]==id:
                        if temp[2]=="deposit":
                            balance=balance+int(temp[3])
                        else:
                            balance=balance-int(temp[3])
        return balance