# Student report :

rno=int(input("Enter student id : "))
name=input("Enter student name : ")
sub1=int(input("Enter math marks : "))
sub2=int(input("Enter science marks : "))
sub3=int(input("Enter computer marks : "))


t=sub1+sub2+sub3
avg=t/3

print("-" * 100)
print("\t\tStudent Progress Report")
print("-" * 100)

print("\t\tRoll no :\t ",rno)
print("\t\tStudent name :\t ",name)
print("\t\tMath marks :\t ",sub1)
print("\t\tScience marks :\t ",sub2)
print("\t\tComputer marks :\t ",sub3)
print ("\t\ttotal :\t ",t)
print("\t\tavg :\t ",avg)


if avg >= 90 :
              print("\t\tgrade : A1")
elif avg >= 80  <90 :
              print("\t\tgrade : A2")
elif avg >= 70 <80 :
              print("\t\tgrade : B1")
elif avg >= 60 <70 :
              print("\t\tgrade : B2")
elif avg >= 50 <60 :
              print("\t\tgrade : C")
else :
              print("\t\tgrade : D")

print("-" * 100)
print("-" * 100)

input()




