#!/usr/bin/python
print(''''********************************************
         Printing a hello message and getting details from user'
***************************************************''')
print("Hello ! Welcome to python program \n")
Total = int(input("Enter total number of students : "))
# Check whether the total value is less than 0
if Total > 0:
    for i in range(Total):
        Student_Name = str(input("Enter Student's Name :"))
        Student_Age = int(input("Enter {0}Student's Age :".format(Student_Name)))
        Student_Address = str(input("Enter {0} address :".format(Student_Name)))
else:
    print("Sorry ! No.of Students was less")
