def hms(s):
    t=s
    h=t//3600
    t=t-(h*3600)
    m=t//60
    t=t-(m*60)
    se=t
    return h,m,se

ti=int(input("Enter the time in sec: "))
print(hms(ti))