class trading:
    def __init__(self,name):
        self.name=name
        self.buyshares=0
        self.rate=0
        self.sellshare=0
        self.sellrate=0

    def buy(self,shares,rate):
        self.buyshares=shares
        self.rate=rate

    def sell(self,shares,rate):
        self.sellrate=rate
        self.sellshare=shares

    def display(self):
        print("Stock trading***")
        print("Name:",self.name)
        print("Purchased {} for {}$= ".format(self.buyshares,self.rate))