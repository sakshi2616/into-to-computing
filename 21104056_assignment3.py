#QUESTION 1
print("PROBLEM-1")
input_string=str(input("Enter any string: "))
list1=input_string.split() 
dict={} 
if list1.__len__()==1:   
    for i in list1[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)   
else:                   
    for i in list1:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
print("\n")


#QUESTION 2
print("PROBLEM-2")
day = int(input("Input a day [1-31]: "))
month = int(input("Input a month [1-12]: "))
year = int(input("Input a year: "))

#finding out if the year is a leap year or not
if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False
#finding the length of month
if month in (1, 3, 5, 7, 8, 10, 12):
    month_duration = 31
elif month == 2:
    if leap_year:
        month_duration = 29
    else:
        month_duration = 28
else:
    month_duration = 30


if day < month_duration:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [dd-mm-yyy] %d/%d/%d." % (day, month, year))
print("\n")


#QUESTION 3
print("PROBLEM-3")
#Python program to create a list of tuples
list=[]
num= int(input("Enter number of elements to be entered in the list:"))
for ele in range(0, num):
    element= int(input("Enter the element:"))
    list.append(element)
print(list)
list_of_tuples=[]
for i in list:
    tuple=(i,i**2)
    list_of_tuples.append(tuple)
print(list_of_tuples)
print("\n")


#Question 4
print("PROBLEM-4")
grade_point=int(input("Enter the grade:"))
letter_grade={ 4:'D', 5:'C',6:'C+',7:'B',8:'B+',9:'A',10:'A+'}
performance={4:'Poor',5:'Below Average',6:'Average',7:'Good',8:'Very Good',9:'Excellent',10:'Outstanding'}
if grade_point<4 or grade_point>10:
    print("ERROR")
else:
    print("Your grade is", letter_grade[grade_point], "and", performance[grade_point], 'performance')
print("\n")



#QUESTION 5
print("PROBLEM-5")
x = 6
for i in range(x):
    for j in range(i):
        print(' ', end='')
    for j in range(2*(x-i)-1):
        print(chr(65 + j), end='')  
    print()
print("\n")



#QUESTION 6
print("PROBLEM-6")
sid = int(input("Enter SID of the student: "))
name = input("Enter Name of the student: ")
student_data = {sid:name}

while True:
    wish = input("Do you wish to enter details of another student?(Y or N): ").upper()
    if wish == 'Y':
        sid = int(input("Enter SID: "))
        name = input("Enter Name: ")
        student_data[sid] = name
    elif wish == 'N':
        break
    else:
     print('Invalid input')


#a-part
print("answer a:" ,student_data)

#b-part
print("answer b:" ,{k:v for k,v in sorted(student_data.items(), key= lambda x:x[1])})

#c-part
print("answer c:" ,{k:v for k,v in sorted(student_data.items())})

#d-part
search = int(input("Please Enter SID of the student: " ))
print("d. Student with given SID is: " ,student_data[search])
print("\n")



#QUESTION 7
print("PROBLEM-7")
# Python program to display the Fibonacci sequence
def fibosequence(n):
   if n <= 1:
       return n
   else:
       return(fibosequence(n-1) + fibosequence(n-2))

terms = int(input("enter a number: "))

# check if the number of terms is valid
if terms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   sum=0
   for i in range(terms):
       print(fibosequence(i))
       sum=sum+fibosequence(i)
#printing average of resultant sequence 
avg=float(sum/terms)
print(avg)
print("\n")


#QUESTION 8
print("PROBLEM-8")
Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}

#part(a)
set_a = (Set1|Set2)-(Set1&Set2)
print("part a answer set: ", set_a)

#part(b)
set_b = (Set1|Set2|Set3) - ((Set1&Set2)|(Set2&Set3)|(Set3&Set1))
print("part b answer set: ", set_b)

#part(c)
set_c= ((Set1&Set2)|(Set1&Set3)|(Set3&Set2))-(Set1&Set2&Set3)
print("part c answer set: ", set_c)

#part(d)
set_d= set()
for i in range(1, 11):
    if i not in Set1:
        set_d.add(i)
print("part d answer set: ", set_d)

#part(e)
set_e = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        set_e.add(i)
print("part e answer set: ", set_e)
