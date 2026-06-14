# WAP to enter marks of a student if marks is greater than 90 enter grade A and so on..
marks=int(input("Enter marks of a student: ", ))
if(marks>=90):
    print("Grade A")
elif(marks >=80 and marks < 90):
    print("Grade B")
elif(marks>=70 and marks <80):
    print("Grade C")
elif(marks>=60 and marks<70):
    print("Grade D")
else:
    print("Fail")
