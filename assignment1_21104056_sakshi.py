#Question 1

num1=int(input("enter a number: "))
num2=int(input("enter a number: "))
num3=int(input("enter a number: "))
avg=(num1+num2+num3)/3
print("the average of these numbers is: ", avg)

#Question 2

x=int(input("enter your gross income: "))
y=int(input("enter number of dependants: "))
z=3000*y
taxable_income= x-10000-z
tax=float(taxable_income)*0.2
print("your tax is: ", tax)

#Question 3

Student= "Student"
SID= 21104056
Name= "Sakshi"
Gender="F"
CourseName=" Intro To Computing"
CGPA=float(8.74)
list=[SID, Name, Gender, CourseName, CGPA]
print(Student, list)

#Question 4

marks_1=int(input("enter your marks: "))
marks_2=int(input("enter your marks: "))
marks_3=int(input("enter your marks: "))
marks_4=int(input("enter your marks: "))
marks_5=int(input("enter your marks: "))
list= [marks_1, marks_2, marks_3, marks_4, marks_5]
list.sort()
print(list)


#Question 5 (a)
list1=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
list1.remove('Black')
print("Color", list1)

#Question 5 (b)
list2=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
list2[3:5]=['Purple']
print(list2)
