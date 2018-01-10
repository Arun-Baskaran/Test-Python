#!/usr/bin/python
# Script to check password lenght
print('''************************************************
    Script to check password lenght entered by user
 ***************************************************''')
Password = input("Enter your password :")
Check_Length = len(Password)
# Compare whether password lenght is greater than 9
if len(Password) < 9:
    print("Password length should be greater than or equal to 9")
else:
    print("Congrats ! Password check passed")

# Trying to print using fstring
Details = f 'Password entered by user is {Password}'
print(Details)
