#!/usr/bin/python
# Basic program for function
# Some Built-in function
# len()             input()
# count()         print()
# find()           type()
# Defining a function


def Details():
    Name = input("Enter your name :")
    print ('''Type your experience level
           1. Beginner
           2. Intermediate
           3. Experience ''')
    Level = str(input("Your Experience Level : "))
    Age = int(input("Enter your age : "))
    if Age < 18 and Level == "Beginner":
        print("Sorry your're not eligible")
    elif Age > 18 and Level == "Intermediate":
        print ("Welcome {0} and your fee per month is Rs . 1000".format(Name))
    elif Age > 18 and Level == "Experience":
        print ("Welcome {0} and your fee per month is Rs . 2000".format(Name))
    else:
        print("Enter your Name,Age,Level properly")


def main():
    Details()


if __name__ == '__main__':
    main()
