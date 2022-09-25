eng = 'English'
tam = 'Tamil'
mat = 'Maths'
sci = 'Science'
soc = 'Social'
mar = 'Mark'
grd = 'Grade'

def getinputs():
        print("Enter the marks...")
        marks[eng][mar] = int(input("English: "))
        marks[tam][mar] = int(input("Tamil: "))
        marks[mat][mar] = int(input("Maths: "))
        marks[sci][mar] = int(input("Science: "))
        marks[soc][mar] = int(input("Social: "))
def grades(m):
    if m>=90 and m<=100:
        return 'A'
    elif m>=80 and m<=89:
        return 'B'
    elif m>=70 and m<=79:
        return 'C'
    elif m>=60 and m<=69:
        return 'D'
    else:
        return 'E'

def average():
    total=marks[tam][mar]+\
          marks[eng][mar] +\
        marks[mat][mar]+\
        marks[sci][mar]+\
        marks[soc][mar]
    return total/5

marks={}
marks[eng]={mar:0, grd:''}
marks[tam]={mar:0, grd:''}
marks[mat]={mar:0, grd:''}
marks[sci]={mar:0, grd:''}
marks[soc]={mar:0, grd:''}
getinputs()
print("Student report card")
print("---------------------")
print("Subject  Mark  Grade")
print("---------------------")
print("{:7s}  {:^4d}  {:^5s}".format('English',marks[eng][mar],grades(marks[eng][mar])))
print("{:7s}  {:^4d}  {:^5s}".format('Tamil',marks[tam][mar],grades(marks[tam][mar])))
print("{:7s}  {:^4d}  {:^5s}".format('Maths',marks[mat][mar],grades(marks[mat][mar])))
print("{:7s}  {:^4d}  {:^5s}".format('Science',marks[sci][mar],grades(marks[sci][mar])))
print("{:7s}  {:^4d}  {:^5s}".format('Social',marks[soc][mar],grades(marks[soc][mar])))
print("---------------------")
print("The average: ",average())