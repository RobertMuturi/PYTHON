#program to check employment and earnings

print("To answer the questions below, please use \n 1 for Yes \n 2 for no")
      
employed = int(input("Are you employed? "))
earning = int(input("Are you earning over Ksh 10,000? "))

if employed == 1 and earning == 1:
    print("You are eligible for taxation")
else:
    print("You are not eligible for taxation")



#else - if statement with pass statement
earning = 20000

if earning > 10000:
    pass
else:
    pass

#program to check stored password against user input

while True:
    password = input("Enter password: ")
    if password[0] == "#" or password[0] == "$" or password[0] == "%":
        print("First character correct.")
    else:
        print("First character wrong.")
        continue
    if password == "python" or password == "python" or password == "python":
        print("Correct password")
        break
    else:
        print("Wrong password")
    print(password)
            
print("Logged in")


