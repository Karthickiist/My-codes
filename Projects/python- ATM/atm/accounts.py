class accounts:
    file="./data/accountlist.txt"
    datas={}
    number=""
    def __init__(self):
        if len(accounts.datas)==0:
            self.load()

    def load(self):
        accounts.datas.clear()
        with open(accounts.file,"r") as f:
            temp=f.readlines()
            for i in temp:
                if i.strip()!="":
                    temp1=i.split(",")
                    accnum=temp1[0].strip()
                    name=temp1[1].strip()
                    pin=temp1[2].strip()
                    accounts.datas[accnum]={"Name":name,"Pin":pin}

    def accountverify(self, accnum):
        if accnum in accounts.datas:
            accounts.number=accnum
            return accounts.datas[accnum]["Name"]
        else:
            raise Exception("Invalid account number.. Try again...")

    def pinverify(self,pin):
        if accounts.datas[accounts.number]["Pin"]==pin:
            return True
        else:
            raise Exception("Invalid pin number.. Try again...")
