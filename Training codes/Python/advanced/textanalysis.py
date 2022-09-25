class textanalysis:
    def __init__(self):
        self.text=""
        self.result={}

    def autotext(self):
        self.text="Python is a high-level, interpreted, general-purpose programming language. " \
                  "Its design philosophy emphasizes code readability with the use of significant " \
                  "indentation. Python is dynamically-typed and garbage-collected."

    def analysis(self):
        self.result.clear()
        temptxt=self.text.lower()
        for i in temptxt:
            if i.isalpha():
                if i in self.result:
                    self.result[i]+=1
                else:
                    self.result[i]=1

    def manualtext(self):
        temptxt=""
        print("Enter the text (press enter twice to process text):")
        while True:
            t=input()
            if len(t)==0:
                break

            temptxt+=t

        self.text=temptxt

    def filepath(self):
        p=input("Enter file path: ")
        with open(p,"r") as f:
            temptxt=f.read()
        self.text=temptxt
        print(self.text)

    def display(self):
        print("The text: {}".format(self.text))
        for i,j in self.result.items():
            print("{} {:4d} {}".format(i,j,"*"*j))