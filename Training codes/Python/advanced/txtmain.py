from textanalysis import textanalysis
a=textanalysis()
while True:
    print("Test Analysis")
    print("1.Automatic Text")
    print("2.Manual Entry")
    print("3.File Read: ")
    print("0.Exit")
    res=int(input("Enter your option: "))
    if res==1:
        a.autotext()
    elif res==2:
        a.manualtext()
    elif res==3:
        a.filepath()
    elif res==0:
        break
    else:
        print("Invalid option try again....")
    a.analysis()
    a.display()

    input("press enter...")
    print()

del a