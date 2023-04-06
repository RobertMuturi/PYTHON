#if
'''
age = int(input("Enter your age: "))

if age > 18:
    print("An adult...")

#if-else
if age > 18:
    print("This is an adult...")
else:
    print("This is a young person")

    
#if-elif-else (age brackets)
if age < 0:
    print("Negative age does not exist")
elif age <= 12: #else if
    print("This is a child")
elif age <= 19: #else if
    print("This is a teenager")
else:
    print("The person is an adult...")
'''
##User password checker

#stored password
password = 2023
passwd = int(input("Enter your password: "))

if passwd == password:
    print("The password is correct...")
else:
    print("You entered the wrong password!")

#Nested if
#Nested if-elif
#Nested if-elif-else
