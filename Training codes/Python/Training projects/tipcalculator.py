print("Welcome to the tip calculator.")
bill=float(input("What was the total bill? $"))
tip=float(input("What percentage of tip would you like to give? 10,12 or 15 :"))
people=int(input("How many people to split the bill? "))
total_tip=bill*(tip/100.0)
total_bill=bill+total_tip
print("Each persion should pay",round(total_bill/float(people)))