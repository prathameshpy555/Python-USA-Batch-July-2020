# Student report :

EmpID=int(input("Enter employee id : "))
EmpName=input("Enter employee name : ")
EmpDesg=(input("Enter employee designation : "))
MonthlySal=int(input("Enter employee's monthly salary in USD : "))

print("-" * 100)
print("\t\t\tEmployee Report")
print("-" * 100)

print("\t\tEmployee id : ",EmpID)
print("\t\tEmployee name : ",EmpName)
print("\t\tEmployee designation : ",EmpDesg)
print("\t\tEmployee's monthly Salary : ",MonthlySal,"dollars")
print("\t\tEmployee's yearly Salary : ",MonthlySal*12,"dollars")


if EmpDesg == 'manager' :
              print("\t\tMonthly salary Bonus : ",(MonthlySal*40/100)+MonthlySal,"dollars")
elif EmpDesg=='analyst' :
               print("\t\tMonthly salary Bonus :",(MonthlySal*30/100)+MonthlySal,"dollars")
elif EmpDesg=='programmer':
               print("\t\tMonthly salary Bonus : ",(MonthlySal*20/100)+MonthlySal,"dollars")
elif EmpDesg=='salesman':
               print("\t\tMonthly salary Bonus : ",(MonthlySal*15/100)+MonthlySal,"dollars")
else:
               print("\t\tMonthly salary Bonus : ",(MonthlySal*10/100)+MonthlySal,"dollars")
             


print("-" * 100)
print("-" * 100)




input()


