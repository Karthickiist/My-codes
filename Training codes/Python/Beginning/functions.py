def circel(r):
    area=(22/7.0)*r*r
    diameter=2*r
    return area,diameter

#main function
r1=float(input("Enter radius 1: "))
r2=float(input("Enter radius 2: "))
ra,di=circel(r1)
result=circel(r2)
print("radius: %.2f area:%.2f diameter:%.2f"%(r1,ra,di))
print("radius: %.2f area:%.2f diameter:%.2f"%(r1,result[0],result[1]))